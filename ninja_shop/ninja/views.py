from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def DefaultView(request):
    return render(request, template_name='DefaultView.html', context=None)


def login(request):
    return None


@login_required
def logout(request):
    return None
