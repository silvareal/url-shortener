# Generated by Django 2.0 on 2018-06-21 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20180621_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickevent',
            name='kirr_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='click', to='shorten.KirrURL'),
        ),
    ]