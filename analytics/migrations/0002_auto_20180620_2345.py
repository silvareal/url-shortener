# Generated by Django 2.0 on 2018-06-21 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='clickevent',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='clickevent',
            name='kirr_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shorten.KirrURL'),
        ),
    ]
