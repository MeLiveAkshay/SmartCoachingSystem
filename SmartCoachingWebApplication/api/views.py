from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from core.models import ContactUs
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from SmartCoachingWebApplication.api import views
def index(request):
    return HttpResponse("Hello api!")

def getContactUs(request):
    contacts = ContactUs.objects.all().values()  # Converts QuerySet to list of dictionaries

    if not contacts:
        return JsonResponse(
            {
                'status': 'error',
                'message': 'No Contact Us data found',
                'status_code': 404,
                'data': []
            },
            status=404
        )
    
    return JsonResponse(
        {
            'status': 'success',
            'message': 'Contact Us data retrieved successfully',
            'status_code': 200,
            'data': list(contacts)
        },
        status=200
    )




@csrf_exempt
def insertContactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not all([name, email, message]):
            return JsonResponse({
                'status': 'error',
                'message': 'Missing required fields',
                'status_code': 400
            }, status=400)

        contact = ContactUs.objects.create(
            name=name,
            email=email,
            message=message
        )
        print(f"Contact Us entry created: {contact}")

        return JsonResponse({
            'status': 'success',
            'message': 'Contact Us entry created successfully',
            'status_code': 201,
            'data': {
                'id': contact.id,
                'name': contact.name,
                'email': contact.email,
                'message': contact.message
            }
        }, status=201)

    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed',
        'status_code': 405
    }, status=405)
