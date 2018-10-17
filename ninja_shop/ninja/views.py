from django.shortcuts import render


def DefaultView(request):
    return render(request, template_name='DefaultView.html', context=None)