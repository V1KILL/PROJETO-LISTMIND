from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from .models import Cliente
import datetime



# Create your views here.
def ViewHome(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        
        if name and start_date and end_date:
            clientes = Cliente.objects.filter(name__icontains=name, date__range=[start_date, end_date]).exclude(status=True)
        elif start_date and end_date:
            clientes = Cliente.objects.filter(date__range=[start_date, end_date]).exclude(status=True)
        else:
            clientes = Cliente.objects.filter(name__icontains=name).exclude(status=True)
    else:
        clientes = Cliente.objects.all().exclude(status=True)
    

    paginator = Paginator(clientes, 1)
    page_number = request.GET.get('page')
    try:
        clientes = paginator.page(page_number)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)

    return render(request, 'index2.html', {'clientes':clientes})


def ViewAddClient(request, name, defeito, opcao, predictedDate, predictedPreco, preco, servico, peca):
    newclient = Cliente.objects.create(name=name, description=defeito, opcao=opcao, predicted_date = predictedDate, predicted_price = predictedPreco, price=preco, execution= servico, executiontwo= peca)
    newclient.save()

    return redirect('/')

def ViewArchived(request):
    clientes = Cliente.objects.filter(status=True)

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
    service = Cliente.objects.get(id=id)
    if status.lower() == 'false':
        service.status = False
    else:
        service.status = True
    service.name = name
    service.description = description 
    service.save()

    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

def ViewClientDelete(request, id):
    client = Cliente.objects.get(id=id)
    client.delete()
    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

def ViewDashBoard(request):
    total_clientes = Cliente.objects.count()

    total_clientes_feitos = Cliente.objects.filter(status=True).count()

    dinheiro_arrecadado = Cliente.objects.filter(status=True)

    soma = 0
    for cliente in dinheiro_arrecadado:
        soma += float(cliente.price) 
    
    porcentagem = total_clientes_feitos * 100 / total_clientes
    
    clientes_com_garantia = Cliente.objects.filter(status=True, date__gte=datetime.datetime.now()-datetime.timedelta(days=90))

    return render(request, 'dashboard.html', {'total_clientes':total_clientes, 'total_clientes_feitos':total_clientes_feitos, 'soma':soma, 'porcentagem':porcentagem, 'clientes_com_garantia':clientes_com_garantia})

def ViewDocument(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'document.html', {'cliente':cliente})