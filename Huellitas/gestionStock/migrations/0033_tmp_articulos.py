# Generated by Django 3.2.3 on 2021-10-29 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0032_alter_articulos_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tmp_Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insert', models.BooleanField()),
                ('articulo_proveedor', models.TextField(blank=True, default='', max_length=30, null=True)),
                ('descripcion', models.TextField(blank=True, default='', max_length=30, null=True)),
                ('precio_costo', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionStock.proveedores')),
            ],
            options={
                'verbose_name_plural': '',
            },
        ),
    ]
