from django.urls import path, include
from . import views


urlpatterns = [
    path('job_post/', views.job_post, name='job_post'),
    path('job_listing/', views.job_listing, name='job_listing'),
    path('job_single/<int:id>/', views.job_single, name='job_single'),
    path('job_update/<int:pk>/', views.JobUpdate.as_view(), name='job_update'),

    path('contacts/', views.FeedbackCreate.as_view(), name='contacts'),
    path('contacts_r/', views.feedback_response, name='contacts_r'),
    path('', views.index, name='index'),
]