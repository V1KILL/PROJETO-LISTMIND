from django.shortcuts import render, HttpResponse

# Create your views here.
def ViewHome(request):
    return HttpResponse('ok')