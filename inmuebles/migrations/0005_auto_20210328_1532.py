# Generated by Django 3.0 on 2021-03-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0004_auto_20210326_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Lote', 'Lote'), ('Oficina', 'Oficina')], max_length=50),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('Ciudad Ojeda', 'Ciudad Ojeda'), ('Tamare', 'Tamare'), ('Tía Juana', 'Tía Juana')], max_length=1000),
        ),
    ]
