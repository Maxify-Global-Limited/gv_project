# Generated by Django 4.1.7 on 2023-03-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctor_induction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doctor_slug',
            field=models.SlugField(default='First name and last name', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]