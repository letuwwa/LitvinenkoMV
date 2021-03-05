from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import JobModel


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        JobModel.objects.create(title='JobTitle', company_name='CompanyName', description='temp',
                                responsibilities='temp', experience='temp', job_location='temp')

    def test_instance(self):
        job = JobModel(title='test', company_name='test')
        self.assertTrue(isinstance(job, JobModel))

    def test_title_and_label(self):
        job = JobModel.objects.get(id=1)
        field_label = job._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название вакансии')

    def test_company_name_and_label(self):
        job = JobModel.objects.get(id=1)
        field_label = job._meta.get_field('company_name').verbose_name
        self.assertEquals(field_label, 'Название компании')

    def test_description_and_label(self):
        job = JobModel.objects.get(id=1)
        field_label = job._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_job_location_and_label(self):
        job = JobModel.objects.get(id=1)
        field_label = job._meta.get_field('job_location').verbose_name
        self.assertEquals(field_label, 'Местоположение')

    def test_get_absolute_url(self):
        job = JobModel.objects.get(id=1)
        self.assertEquals(job.get_absolute_url(), '/job_single/1/')

    def test_user_creation(self):
        user = get_user_model().objects.create_user(username='test',
                                                    password='user123U',
                                                    email='testing@example.com')
        user.save()
        job = JobModel.objects.create(user=user, title='JobTitle',
                                      company_name='CompanyName',
                                      description='temp')
        self.assertEqual(job.user, user)
