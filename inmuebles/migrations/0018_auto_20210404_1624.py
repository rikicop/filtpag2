# Generated by Django 2.2 on 2021-04-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0017_auto_20210402_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='image',
            field=models.FileField(blank=True, upload_to='here/2021/04/04'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='posting',
            field=models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Lote', 'Lote'), ('Oficina', 'Oficina'), ('Comercial', 'Comercial')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='inmuebleimage',
            name='images',
            field=models.FileField(upload_to='here/images/2021/04/04'),
        ),
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Lote', 'Lote'), ('Oficina', 'Oficina'), ('Comercial', 'Comercial')], max_length=1000),
        ),
    ]
