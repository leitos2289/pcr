# Generated by Django 2.0 on 2018-11-30 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0004_auto_20181130_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(db_column='CEDULA', max_length=10),
        ),
        migrations.AlterField(
            model_name='persona',
            name='direccion',
            field=models.CharField(blank=True, db_column='DIRECCION', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(db_column='NOMBRE', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tefefono',
            field=models.CharField(blank=True, db_column='TELEFONO', max_length=100),
        ),
    ]
