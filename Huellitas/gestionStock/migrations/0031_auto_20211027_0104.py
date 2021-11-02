# Generated by Django 3.2.3 on 2021-10-27 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0030_auto_20211026_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion_columnas',
            name='miles',
        ),
        migrations.AlterField(
            model_name='articulos',
            name='precio_costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='precio_vta',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='proveedor',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='gestionStock.proveedores'),
        ),
    ]