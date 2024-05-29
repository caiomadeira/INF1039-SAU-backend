
from django.template import loader
from django.http import HttpResponse


def status_api(request):
    return HttpResponse({ "<h1>SAU Backend API</h1>" })