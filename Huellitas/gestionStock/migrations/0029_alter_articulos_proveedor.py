# Generated by Django 3.2.3 on 2021-10-25 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0028_alter_articulos_articulo_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='proveedor',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='gestionStock.proveedores'),
        ),
    ]