from django.contrib import admin
from .models import  Cliente, Serviços
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'price', 'description', 'date')
    search_fields = ('name', 'phonenumber')
    list_filter = ('date',)