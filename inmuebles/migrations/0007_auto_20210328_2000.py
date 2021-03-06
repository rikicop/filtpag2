# Generated by Django 2.2 on 2021-03-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0006_auto_20210328_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='edo',
            field=models.CharField(blank=True, choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado')], max_length=1000),
        ),
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
