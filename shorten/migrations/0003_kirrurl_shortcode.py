# Generated by Django 2.0 on 2018-06-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0002_auto_20180613_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(default='fdfd', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]