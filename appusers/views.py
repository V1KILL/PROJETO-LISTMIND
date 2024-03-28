from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Cliente
# Create your views here.
def ViewHome(request):

    clientes_list = Cliente.objects.all()
    items_por_pagina = 2
    paginator = Paginator(clientes_list, items_por_pagina)
    page_number = request.GET.get('page')
    try:
        clientes = paginator.page(page_number)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)
    
    return render(request, 'index.html', {'clientes':clientes})

def ViewAddClient(request, name, phonenumber, price, description):
    newclient = Cliente.objects.create(name=name, phonenumber=phonenumber, price=price, description=description)
    newclient.save()

    return redirect('/')