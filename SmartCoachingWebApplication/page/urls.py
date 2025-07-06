from django.urls import path

from SmartCoachingWebApplication.page import views

urlpatterns = [
    path('', views.index, name='index'),
]