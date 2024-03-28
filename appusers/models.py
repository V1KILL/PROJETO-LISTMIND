from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = PhoneNumberField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

class Serviços(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)