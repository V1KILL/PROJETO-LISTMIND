from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Cliente



# Create your views here.
def ViewHome(request):
    

    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 2)
    page_number = request.GET.get('page')
    clientes = paginator.page(page_number)
    
    
    return render(request, 'index.html', {'clientes':clientes})

def ViewAddClient(request, name, phonenumber, price, description):
    newclient = Cliente.objects.create(name=name, phonenumber=phonenumber, price=price, description=description)
    newclient.save()

    return redirect('/')

def ViewFilter(request):
    if request.method == 'POST':
        name = request.POST['name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        
        if name and start_date and end_date:
            clientes = Cliente.objects.filter(name__icontains=name,date__range=[start_date, end_date])
        elif start_date and end_date:
            clientes = Cliente.objects.filter(date__range=[start_date, end_date])
        else:
            clientes = Cliente.objects.filter(name__icontains=name)
        
        
        return render(request, 'index.html', {'clientes':clientes})
    return render(request, 'index.html')