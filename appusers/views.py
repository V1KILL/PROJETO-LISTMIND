from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from .models import Cliente
import datetime
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
# Create your views here.

def ViewSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Nome Existente')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, 'Conta Criada com Sucesso')
                return redirect('signin')
        else:
            messages.info(request, 'Senhas não coincidem')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def ViewSignin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            auth.login(request, user)
            return redirect('/')
        elif user is not None and not user.check_password(password):
            messages.info(request, 'Senha incorreta')
            return redirect('signin')
        else:
            messages.info(request, 'Usuário Não existe')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
    
@login_required(login_url='/signin')
def ViewLogout(request):
    logout(request)
    return redirect('signin')

def ViewHome(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        
        if name and start_date and end_date:
            clientes = Cliente.objects.filter(user=request.user,name__icontains=name, date__range=[start_date, end_date]).exclude(status=True)
        elif start_date and end_date:
            clientes = Cliente.objects.filter(user=request.user,date__range=[start_date, end_date]).exclude(status=True)
        else:
            clientes = Cliente.objects.filter(user=request.user,name__icontains=name).exclude(status=True)
    else:
        clientes = Cliente.objects.filter(user=request.user).exclude(status=True)
    

    paginator = Paginator(clientes, 5)
    page_number = request.GET.get('page')
    try:
        clientes = paginator.page(page_number)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)

    return render(request, 'index2.html', {'clientes':clientes})


def ViewAddClient(request, name, defect, option, predicted_date, predicted_price, price, service, part):
    newclient = Cliente.objects.create(name=name, defect=defect, option=option, predicted_date = predicted_date, predicted_price = predicted_price, price=price, service= service, part= part, user=request.user)
    newclient.save()

    return redirect('/')

def ViewArchived(request):
    clientes = Cliente.objects.filter(status=True,user=request.user)

    paginator = Paginator(clientes, 5)
    page_number = request.GET.get('page')
    try:
        clientes = paginator.page(page_number)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)
    query = True
    return render(request, 'index2.html', {'clientes':clientes, 'query':query})

def ViewServiceEdit(request, status, id,name, description):
    service = Cliente.objects.get(id=id,user=request.user)
    if status.lower() == 'false':
        service.status = False
    else:
        service.status = True
    service.name = name
    service.defect = description 
    service.save()

    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

def ViewClientDelete(request, id):
    client = Cliente.objects.get(id=id,user=request.user)
    client.delete()
    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

def ViewDashBoard(request):
    clients = Cliente.objects.filter(user=request.user)
    done_clients = clients.filter(status=True)

    money = 0
    for cliente in done_clients:
        money += float(cliente.price) 
    
    pendents_clients= clients.filter(status=True, date__gte=datetime.datetime.now()-datetime.timedelta(days=90))
    meses = clients.values('date__month').annotate(total_arrecadado=Sum('price')).filter(status=True)

    faturamento = [0] * 12

    for mes in meses:
        indice = mes['date__month'] - 1

        faturamento[indice] = int(mes['total_arrecadado'])

    
    return render(request, 'dashboard.html', {'clients':clients, 'done_clients':done_clients, 'money':money,'pendent_clients':pendents_clients, 'faturamento':faturamento})


def ViewDocument(request, id):  
    cliente = Cliente.objects.get(id=id, user=request.user)
    html = render_to_string('document.html', {'cliente': cliente})
    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('Ocorreu um erro ao gerar o PDF')

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="documento.pdf"'
    return response


def ViewGarantidos(request):
    clientes = Cliente.objects.filter(status=True, user=request.user, date__gte=datetime.datetime.now()-datetime.timedelta(days=90))
    
    paginator = Paginator(clientes, 5)
    page_number = request.GET.get('page')
    try:
        clientes = paginator.page(page_number)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)
    return render(request, 'garantia.html', {'clientes':clientes})