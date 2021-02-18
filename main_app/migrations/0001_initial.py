# Generated by Django 3.1.6 on 2021-02-18 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя')),
                ('text', models.TextField(max_length=1024, verbose_name='Текст')),
                ('email', models.EmailField(max_length=256, verbose_name='Почта для ответа')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('employment_status', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Freelance', 'Freelancer')], max_length=10)),
                ('description', models.TextField()),
                ('responsibilities', models.TextField()),
                ('experience', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=120)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('published_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
