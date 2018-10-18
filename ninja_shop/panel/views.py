"""
:module ninja.panel.views

This module consists of views regarding basic admin panel, as stated in the
task documentation.

The reason why we are using function views instead of class views is because
built-in django functions do not allow to manipulate views in manner, especially
does not allow advanced validation out of the box.

Also, each view is secured to be viewed only by staff members.

This file is considered that shall be small and concise and provide basic logic
about views so each controller logic has been put into submodule validators.

Why Class Views are not used? Because function views are easier to control and are more extensible and allows us
to use advanced decorators that may be written.
"""

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from exchange.models import Category
from exchange.models import Product, Order


def panel_login(request):
    """

    :param request: HttpRequest
    :return: login screen if user is not authenticated, else main screen of admin panel (type of: HttpResponse)
    """
    if request.method == "GET":
        context = {}
        if request.user.is_authenticated():
            context['UserEmail'] = request.user.email
            context['UserName'] = request.user.username
            return render(request, 'panel/panel_welcome.html')
        else:
            return render(request, 'panel/login.html', context)
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error': 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('panel_default')
        else:
            return render(request, 'panel/login.html',
                          context={'Error': 'Credentials were not correct. Please try again.'})


@staff_member_required
def product_remove(request, index):
    """

    :param request:
    :param index:
    :return:
    """

    if request.method == "GET":
        try:
            context = {}
            context['Product'] = Product.objects.get(pk=index)
            return render(request, 'panel/remove_product_request.html', context)
        except:
            return render(request, 'panel/removal_unsuccessful.html')

    if request.method == "POST":
        try:
            Product.objects.delete(pk=index)
            return render(request, 'panel/removal_successful.html')
        except:
            return render(request, 'panel/removal_unsuccessful.html')


@staff_member_required
def product_edit(request, index):
    context['Product'] = Product.objects.get(pk=index)
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        return render(request, 'panel/panel_product_edit.html')

    if request.method == "POST":
        context['Product'].Title = request.POST.get('Title')
        context['Product'].Image = request.POST.get('Image')
        context['Product'].Description = request.POST.get('Description')
        context['Product'].Price = float(request.POST.get('Price'))
        return render(request, 'panel/edit_success.html')


@staff_member_required
def product_view(request, index):
    """

    :param request:
    :param index:
    :return:
    """
    context = {
        'Product': Product.object.get(pk=index)
    }
    if request.method == "GET":
        return render(request, 'panel/panel_product_view.html', context=context)


@staff_member_required
def product_add(request):
    context = {
        'Product': Product()
    }
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'panel/panel_product_add.html')

    if request.method == "POST":
        context['Product'].Title = request.POST.get('Title')
        context['Product'].Image = request.POST.get('Image')
        context['Product'].Description = request.POST.get('Description')
        context['Product'].Price = float(request.POST.get('Price'))
        return render(request, 'panel/edit_success.html')


@staff_member_required
def product_list(request):  # Todo logic
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        context = {
            'Products': Product.objects.all()
        }
        return render(request, 'panel/product_list.html')
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error': 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('PanelMain')
        else:
            return render(request, 'panel/login.html',
                          context={'Error': 'Credentials were not correct. Please try again.'})


@staff_member_required
def order_remove(request, index):
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        try:
            context = {
                'Order': Order.objects.get(pk=index)
            }
            return render(request, 'panel/remove.html', context)
        except:
            return render(request, 'panel/removal_unsuccessful.html')

    if request.method == "POST":
        try:
            order = Order.objects.delete(pk=index)
            order.delete()
            return render(request, 'panel/removal_successful.html')
        except:
            return render(request, 'panel/removal_unsuccessful.html')


@staff_member_required
def order_edit(request, index):
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        try:
            context = {
                'Order': Order.objects.get(pk=index)
            }
        except:
            context = {
                'Error': 'Not Found'
            }
        return render(request, 'panel/order_edit.html', context)  # TODO TEMPLATE

    if request.method == "POST":
        order = Order.objects.get(pk=index)
        order.Product.pk = request.POST.get('Product')
        order.Count = int(request.POST.get('Count'))
        order.MethodOfDelivery.pk = int(request.POST.get('MethodOfDelivery'))
        order.save()
        return render(request, 'panel/order_edit_success.html', context)


@staff_member_required
def order_add(request):  # Todo: Logic
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        context = {}
        pass
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error': 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('PanelMain')
        else:
            return render(request, 'panel/login.html',
                          context={'Error': 'Credentials were not correct. Please try again.'})


@staff_member_required
def order_view(request, index):  # Todo: Logic
    if request.method == "GET":
        context = {}
        context['Order'] = Order.objects.get(pk=index)
        pass
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error': 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('PanelMain')
        else:
            return render(request, 'panel/login.html',
                          context={'Error': 'Credentials were not correct. Please try again.'})


@staff_member_required
def order_list(request):  # Todo Logic
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        context = {
            'Orders' : Order.objects.all()
        }
        for order in context['Orders']:
            order.Total = order.Product.Price * order.Count + order.MethodOfDelivery.Price


        return render(request, 'panel/order_list.html', context)
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error': 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('PanelMain')
        else:
            return render(request, 'panel/login.html',
                          context={'Error': 'Credentials were not correct. Please try again.'})


@staff_member_required
def category_view(request, index):  # Todo Logic
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        context = {}
        context['Categories'] = Category.objects.get(pk=index)
    if request.method == "POST":
        return render(request, 'panel/edit_success.html')


@staff_member_required
def category_remove(request, index):
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        try:
            context = {}
            context['Entity'] = Category.objects.get(pk=index)
            return render(request, 'panel/remove.html', context)
        except:
            return render(request, 'panel/removal_unsuccessful.html')

    if request.method == "POST":
        return render(request, 'panel/edit_success.html')


@staff_member_required
def category_edit(request, index):  # TODO
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        context = {}
        context['Entity'] = Category.objects.get(pk=index)
        pass
    if request.method == "POST":
        return render(request, 'panel/edit_success.html')


@staff_member_required
def category_add(request):  # TODO
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        context = {}
        pass
    if request.method == "POST":
        return render(request, 'panel/edit_success.html')


@staff_member_required
def category_list(request):  # TODO
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        context = {}
        context['Entity'] = Category.objects.all()
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error': 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('PanelMain')
        else:
            return render(request, 'panel/login.html',
                          context={'Error': 'Credentials were not correct. Please try again.'})


@staff_member_required
def delivery_method_view(request, index):  # TODO
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        context = {}
        context['Entity'] = DeliveryMethod.objects.get(pk=index)
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error': 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('PanelMain')
        else:
            return render(request, 'panel/login.html',
                          context={'Error': 'Credentials were not correct. Please try again.'})


@staff_member_required
def delivery_method_remove(request, index):  # TODO
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        try:
            context = {}
            context['Entity'] = DeliveryType.objects.get(pk=index)
            return render(request, 'panel/remove.html', context)
        except:
            return render(request, 'panel/removal_unsuccessful.html')

    if request.method == "POST":
        try:
            DeliveryType.objects.delete(pk=index)
            return render(request, 'panel/removal_successful.html')
        except:
            return render(request, 'panel/removal_unsuccessful.html')


@staff_member_required
def delivery_method_edit(request, index):  # TODO
    """

    :param request:
    :param index:
    :return:
    """
    if request.method == "GET":
        context = {}
        context['Entity'] = DeliveryMethod.objects.get(pk=index)
        pass
    if request.method == "POST":
        return render(request, 'panel/edit_success.html')


@staff_member_required
def delivery_method_add(request):  # TODO
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        context = {}
        context['Entity'] = DeliveryMethod.objects.get(pk=index)
    if request.method == "POST":
        return render(request, 'panel/edit_success.html')


@staff_member_required
def delivery_method_list(request):  # TODO
    """

    :param request:
    :return:
    """
    if request.method == "GET":
        context = {}
        context['Entity'] = DeliveryMethod.objects.all()
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error': 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('PanelMain')
        else:
            return render(request, 'panel/login.html',
                          context={'Error': 'Credentials were not correct. Please try again.'})
