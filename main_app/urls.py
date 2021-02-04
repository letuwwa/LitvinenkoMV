from django.urls import path, include
from . import views


urlpatterns = [
    path('contacts/', views.FeedbackCreate.as_view(), name='contacts'),
    path('', views.index, name='index'),
]