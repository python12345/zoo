# Generated by Django 2.0.1 on 2018-05-30 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cellular', '0003_auto_20180530_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barzel',
            name='btype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cellular.BarzelType', verbose_name='Barzel type'),
        ),
        migrations.AlterField(
            model_name='barzel',
            name='imei',
            field=models.CharField(max_length=20, null=True, verbose_name='IMEI'),
        ),
    ]
