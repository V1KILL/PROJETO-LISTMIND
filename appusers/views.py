from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from .models import Cliente
import datetime
from plotly.offline import plot
import plotly.graph_objs as go

from django.db.models import Sum
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
    newclient = Cliente.objects.create(name=name, defect=defect, option=option, predicted_date = predicted_date, predicted_price = predicted_price, price=price, service= service, part= part)
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
    service.defect = description 
    service.save()

    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

def ViewClientDelete(request, id):
    client = Cliente.objects.get(id=id)
    client.delete()
    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

def ViewDashBoard(request):
    clients = Cliente.objects.all()
    done_clients = Cliente.objects.filter(status=True)

    money = 0
    for cliente in done_clients:
        money += float(cliente.price) 
    
    pendents_clients= Cliente.objects.filter(status=True, date__gte=datetime.datetime.now()-datetime.timedelta(days=90))
    meses = Cliente.objects.values('date__month').annotate(total_arrecadado=Sum('price')).filter(status=True)

    faturamento = [0] * 12

    for mes in meses:
        indice = mes['date__month'] - 1  # Subtrai 1 para ajustar o índice da lista
        faturamento[indice] = int(mes['total_arrecadado'])

    
    return render(request, 'dashboard.html', {'clients':clients, 'done_clients':done_clients, 'money':money,'pendent_clients':pendents_clients, 'faturamento':faturamento})


def ViewDocument(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'document.html', {'cliente':cliente})

def ViewGarantidos(request):
    clientes = Cliente.objects.filter(status=True, date__gte=datetime.datetime.now()-datetime.timedelta(days=90))
    
    paginator = Paginator(clientes, 5)
    page_number = request.GET.get('page')
    try:
        clientes = paginator.page(page_number)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)
    return render(request, 'garantia.html', {'clientes':clientes})