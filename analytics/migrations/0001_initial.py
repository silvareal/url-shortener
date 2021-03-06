# Generated by Django 2.0 on 2018-06-20 13:00

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shorten', '0007_auto_20180620_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('kirr_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shorten.KirrURL')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
