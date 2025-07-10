from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("College Manage+ment System")


def insertContactUs(request):
    return render(request, 'contact.html')    