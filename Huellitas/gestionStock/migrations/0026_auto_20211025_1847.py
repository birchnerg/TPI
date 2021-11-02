# Generated by Django 3.2.3 on 2021-10-25 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0025_auto_20211018_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion_columnas',
            name='cant_caracteres',
        ),
        migrations.RemoveField(
            model_name='configuracion_columnas',
            name='tipo_dato',
        ),
        migrations.AlterField(
            model_name='articulos',
            name='tipo',
            field=models.TextField(choices=[('Alimento', 'Alimento'), ('Ropa', 'Ropa'), ('Accesorio', 'Accesorio')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion_columnas',
            name='columna_archivo',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='configuracion_columnas',
            name='columna_bd',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='configuracion_columnas',
            name='decimal',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion_columnas',
            name='miles',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='localidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionStock.localidades'),
        ),
    ]