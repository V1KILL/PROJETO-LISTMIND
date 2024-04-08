from django.contrib import admin
from .models import  Cliente
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('opcao', 'name',  'price', 'description', 'date','predicted_date', 'id')
    search_fields = ('name', 'phonenumber')
    list_filter = ('date',)