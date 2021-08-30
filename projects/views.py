from django.http.response import HttpResponse
def project(request):
    return HttpResponse('HTTP')

def user(request,username):
    return HttpResponse('Http')

def get_id(request,id):
    if id > 10:
        return HttpResponse('HHHH')
    else:
        return HttpResponse('ddddd')