# Generated by Django 4.0.3 on 2022-05-26 14:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mistock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneda',
            name='descripcion',
            field=models.CharField(help_text='Descripción de la Marca', max_length=30),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='simbolo',
            field=models.CharField(help_text='Simbolo de la Moneda', max_length=3),
        ),
        migrations.AlterUniqueTogether(
            name='moneda',
            unique_together={('descripcion', 'uc')},
        ),
    ]
