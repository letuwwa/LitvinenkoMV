from django.urls import path, include
from . import views


urlpatterns = [
    path('job_post/', views.job_post, name='job_post'),
    path('job_listing/', views.job_listing, name='job_listing'),
    path('job_single/<int:id>/', views.job_single, name='job_single'),
    path('job_update/<int:pk>/', views.JobUpdate.as_view(), name='job_update'),
    path('job_delete/<int:pk>/', views.JobDelete.as_view(), name='job_delete'),
    path('my_jobs_list/', views.my_jobs_list, name='my_jobs_list'),

    path('apply_job/<int:pk>/', views.apply_job, name='apply_job'),
    path('response_single/<int:id>/', views.response_single, name='response_single'),
    path('response_update/<int:pk>/', views.ResponseUpdateByEmployee.as_view(), name='response_update'),
    path('response_delete/<int:pk>/', views.ResponseDelete.as_view(), name='response_delete'),
    path('my_responses_list/', views.my_responses_list, name='my_responses_list'),

    path('contacts/', views.FeedbackCreate.as_view(), name='contacts'),
    path('contacts_r/', views.feedback_response, name='contacts_r'),
    path('', views.index, name='index'),
]