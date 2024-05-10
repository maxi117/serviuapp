# Generated by Django 5.0.6 on 2024-05-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviuApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsidio',
            name='ahorro',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='ano_ejecucion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='ano_programa',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='num_giro',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='num_ingreso_ofpa',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='num_resolucion_pago',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='porcentaje_avance_cuota',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='uf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='valor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='valor_miles',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subsidio',
            name='valor_uf_utilizado',
            field=models.IntegerField(),
        ),
    ]
