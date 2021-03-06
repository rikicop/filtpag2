# Generated by Django 2.2 on 2021-04-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0011_auto_20210401_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='post',
            name='details',
        ),
        migrations.RemoveField(
            model_name='post',
            name='detailsTitle',
        ),
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='image',
            field=models.FileField(blank=True, upload_to='here/2021/04/02'),
        ),
        migrations.AlterField(
            model_name='inmuebleimage',
            name='images',
            field=models.FileField(upload_to='here/images/2021/04/02'),
        ),
    ]
