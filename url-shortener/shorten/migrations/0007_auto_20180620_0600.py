# Generated by Django 2.0 on 2018-06-20 13:00

from django.db import migrations, models
import shorten.validation


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0006_kirrurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=300, validators=[shorten.validation.validate_url]),
        ),
    ]
