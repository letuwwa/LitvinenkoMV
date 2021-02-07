from django.urls import path, include
from . import views


urlpatterns = [
    path('contacts/', views.FeedbackCreate.as_view(), name='contacts'),
    path('contacts_r/', views.feedback_response, name='contacts_r'),
    path('', views.index, name='index'),
]