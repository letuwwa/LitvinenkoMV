from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ROLES = [
        ('employer', 'Ищу сотрудников!'),
        ('employee', 'Ищу работу!'),
    ]
    role = models.CharField(max_length=32, blank=False, choices=ROLES, verbose_name='Чего хотите?', null=True)
