from django.db import models
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):
    
    escolhas = {
        ('0', 'Serviço'),
        ('1', 'Diagnóstico'),
        ('2', 'Compra'),
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    opcao = models.CharField(max_length=11, choices=escolhas, default='0')
    date = models.DateTimeField(auto_now_add=True)
    predicted_date = models.DateField(default='2006-02-22')
    predicted_price = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    execution = models.TextField()
    executiontwo = models.TextField()
    status = models.BooleanField(default=False)

    
    def formatted_date(self):
        return self.date.strftime("%d, %B, %Y")
    
    def get_absolute_url(self):
        return [self.id, self.status, self.name, self.description]