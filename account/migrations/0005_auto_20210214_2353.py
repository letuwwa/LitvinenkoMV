# Generated by Django 3.1.6 on 2021-02-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('employer', 'Ищу сотрудников!'), ('employee', 'Ищу работу!')], max_length=32, null=True, verbose_name='Чего хотите?'),
        ),
    ]
