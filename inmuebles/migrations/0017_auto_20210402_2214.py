# Generated by Django 2.2 on 2021-04-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0016_remove_inmueble_enlace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Lote', 'Lote'), ('Oficina', 'Oficina')], max_length=1000),
        ),
    ]