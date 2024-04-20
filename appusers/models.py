from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Cliente(models.Model):
    
    choices = {
        ('0', 'Serviço'),
        ('1', 'Diagnóstico'),
        ('2', 'Compra'),
    }
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    defect = models.TextField()
    option = models.CharField(max_length=11, choices=choices, default='0')
    date = models.DateField(auto_now_add=True)
    predicted_date = models.DateField(default='2006-02-22')
    predicted_price = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service = models.TextField()
    part = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Serviço {self.name} de {self.user}"