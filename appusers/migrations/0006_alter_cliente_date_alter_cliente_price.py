# Generated by Django 5.0.3 on 2024-04-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0005_alter_cliente_opcao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
