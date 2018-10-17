from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


def DefaultView(request):
    return render(request, template_name='DefaultView.html', context=None)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({

    })