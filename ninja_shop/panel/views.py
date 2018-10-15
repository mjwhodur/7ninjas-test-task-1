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
"""

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from panel.validators import user, deliveryaddress, contractor, deliverymethod, order, prices


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
            return render(request, 'panel_welcome.html')
        else:
            return render(request, 'panel/login.html', context)
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if request.POST.get('username') == '' or request.POST.get('password') == '':
            return render(request, 'panel/login.html', context={'Error' : 'Please provide username and password'})

        if user is not None:
            login(request, user)
            return redirect('PanelMain')
        else:
            return render(request, 'panel/login.html', context={'Error' : 'Credentials were not correct. Please try again.'})

@staff_member_required
def category_add(request):
    """
    Adding category view
    :param request: HttpRequest - Incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def category_edit(request, category):
    """
    Edit category view
    :param request: HttpRequest - Incoming request
    :param category: int
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def category_remove(request):
    """
    Remove category view
    :param request: HttpRequest - Incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def product_add(request):
    """
    Add product view
    :param request: HttpRequest - Incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def product_edit(request):
    """
    Edit product data view
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def product_remove(request):
    """
    Remove product view
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def currency_add(request):
    """
    Add currency view
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    pass


@staff_member_required
def currency_edit(request):
    """
    Edit currency view
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def currency_remove(request):
    """
    Remove currency view
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def orders_list(request):
    """
    List orders view
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass


@staff_member_required
def orders_add(request):
    """
    Add orders view
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return order.validate_add(request)


@staff_member_required
def orders_edit(request):
    """
    Edit order with id... view
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return order.validate_edit(request)


@staff_member_required
def orders_remove(request):
    """
    Remove order with id...
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return order.validate_remove(request)


@staff_member_required
def orders_fullfill(request):
    """
    Fullfill order with ID and set its state to 'fulfilled'
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return order.validate_fullfil(request)


@staff_member_required
def deliverymethod_list(request):
    """
    Show delivery methods with their prices
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return deliverymethod.validate_list(request)


@staff_member_required
def deliverymethod_add(request):
    """
    Add delivery methods
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return deliverymethod.validate_add(request)


@staff_member_required
def deliverymethod_edit(request):
    """
    Edit delivery methods
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return deliverymethod.validate_edit(request)


@staff_member_required
def deliverymethod_remove(request):
    """
    Remove delivery methods
    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return deliverymethod.validate_remove(request)


@staff_member_required
def contractor_add(request):
    """

    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return contractor.validate_add(request)


@staff_member_required
def contractor_edit(request):
    """

    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return contractor.validate_edit(request)


@staff_member_required
def contractor_remove(request):
    """

    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return contractor.validate_remove(request)


@staff_member_required
def contractor_list(request):
    """

    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return contractor.validate_list(request)


@staff_member_required
def deliveryaddress_add(request):
    """

    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return deliveryaddress.validate_add(request)


@staff_member_required
def deliveryaddress_edit(request):
    """

    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return deliveryaddress.validate_edit(request)


@staff_member_required
def deliveryaddress_remove(request):
    """

    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return deliveryaddress.validate_remove(request)


@staff_member_required
def deliveryaddress_list(request):
    """

    :param request: HttpRequest - incoming request
    :return: HttpResponse
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return deliveryaddress.validate_list(request)

@staff_member_required
def set_prices_for_product(request, product_index):
    """

    :param request:
    :param product_index:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        return prices.validate(request, product_index)