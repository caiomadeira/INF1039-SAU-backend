
from django.template import loader
from django.http import HttpResponse


def api_home(request):
    template = loader.get_template('index.html')
    context = {
        'title': 'SAU Api Home',
        'body_title': 'Rotas da API - SAU',
        'login_route': 'api/v1/auth/login',
         'register_route': 'api/v1/auth/register',
        'absences_route': 'api/v1/student/absences',
        'classes_route': 'api/v1/student/classes',
    }
    return HttpResponse(template.render(context, request))

def login_test(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())