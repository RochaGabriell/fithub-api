# Generated by Django 4.2.6 on 2023-11-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='abdomen',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Abdômen'),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='chest',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Peito'),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='hip',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Quadril'),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='shoulder',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Ombro'),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='waist',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cintura'),
        ),
    ]
