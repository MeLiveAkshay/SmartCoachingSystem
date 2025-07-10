from django.urls import path

from SmartCoachingWebApplication.api import views

urlpatterns = [
    path('api/', views.index, name='index'),
    path('api/contactus/', views.getContactUs, name='get_contact_us'),
    path('api/contactus/insert/', views.insertContactUs, name='insert_contact_us'),
]