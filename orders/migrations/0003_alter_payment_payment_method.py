# Generated by Django 4.1.7 on 2023-03-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_ordereditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('Monnify', 'Monnify'), ('Paystack', 'Paystack')], max_length=100),
        ),
    ]