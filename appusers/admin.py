from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')  # Exibir a data de criação na lista de clientes
    
admin.site.register(Cliente, ClienteAdmin)