from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Cliente(models.Model):
    OPCAO_1 = 'opcao1'
    OPCAO_2 = 'opcao2'
    OPCAO_3 = 'opcao3'

    OPCOES_ESCOLHA = [
        (OPCAO_1, 'Opção 1'),
        (OPCAO_2, 'Opção 2'),
        (OPCAO_3, 'Opção 3'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    opcao = models.CharField(max_length=10, choices=OPCOES_ESCOLHA)
    date = models.DateTimeField(auto_now_add=True)
    predicted_date = models.DateField(default='2006-02-22')
    predicted_price = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    execution = models.TextField()
    executiontwo = models.TextField()
    status = models.BooleanField(default=False)

    phonenumber = PhoneNumberField()
    def formatted_date(self):
        return self.date.strftime("%d, %B, %Y")