# Generated by Django 3.1.6 on 2021-02-04 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя')),
                ('text', models.TextField(max_length=1024, verbose_name='Текст')),
                ('email', models.EmailField(max_length=256, verbose_name='Почта для ответа')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]