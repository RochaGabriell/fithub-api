# Generated by Django 4.2.6 on 2023-11-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='default',
            field=models.BooleanField(default=False, help_text='Se marcado, este treino será o padrão para aparecer na página inicial', verbose_name='Padrão'),
        ),
    ]