# Generated by Django 3.2.3 on 2021-06-28 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0003_auto_20210628_0056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salidas',
            options={'verbose_name_plural': 'Salidas'},
        ),
        migrations.RenameField(
            model_name='altas',
            old_name='proveedor',
            new_name='proveedor_id',
        ),
    ]
