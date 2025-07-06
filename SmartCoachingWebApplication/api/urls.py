from django.urls import path

from SmartCoachingWebApplication.api import views

urlpatterns = [
    path('api/', views.index, name='index'),
]