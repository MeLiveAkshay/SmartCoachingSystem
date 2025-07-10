from django.http import HttpResponse

def index(request):
    return HttpResponse("College Manage+ment System")
