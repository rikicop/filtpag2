# Generated by Django 3.0 on 2021-03-25 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inmueble',
            name='image',
        ),
        migrations.DeleteModel(
            name='InmuebleImage',
        ),
    ]
