from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


def DefaultView(request):
    return render(request, template_name='DefaultView.html', context=None)

def login(request):
    return None

@login_required
def logout(request):
    return None