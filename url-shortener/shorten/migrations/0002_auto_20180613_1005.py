# Generated by Django 2.0 on 2018-06-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]