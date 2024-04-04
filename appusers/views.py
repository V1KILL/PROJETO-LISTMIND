from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from .models import Cliente



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

    return render(request, 'index.html', {'clientes':clientes})


def ViewAddClient(request, name, phonenumber, price, description):
    newclient = Cliente.objects.create(name=name, phonenumber=phonenumber, price=price, description=description)
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
    return render(request, 'index.html', {'clientes':clientes, 'query':query})

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
    return render(request, 'dashboard.html')
