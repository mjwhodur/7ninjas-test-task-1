from django.http import HttpResponse
from . import paint

def registration_view(request):
    return HttpResponse('This feature has not yet been implemented')
    #return paint.registration_view(request, context, status)