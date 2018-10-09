"""
:module ninja.panel.views

This module consists of views regarding basic admin panel, as stated in the
task documentation.

The reason why we are using function views instead of class views is because
built-in django functions do not allow to manipulate views in manner, especially
does not allow advanced validation out of the box.

Also, each view is secured to be viewed only by staff members.
"""

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def panel_login(request):
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def category_add(request):
    """
    Adding category view
    :param request: HttpRequest
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def category_edit(request, category):
    """
    Edit category view
    :param request: HttpRequest
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
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def product_add(request):
    """
    Add product view
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def product_edit(request):
    """
    Edit product data view
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def product_remove(request):
    """
    Remove product view
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def currency_add(request):
    """
    Add currency view
    :param request:
    :return:
    """
    pass

@staff_member_required
def currency_edit(request):
    """
    Edit currency view
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def currency_remove(request):
    """
    Remove currency view
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def orders_list(request):
    """
    List orders view
    :param request:
    :return:
    """
    pass

@staff_member_required
def orders_add(request):
    """
    Add orders view
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def orders_edit(request):
    """
    Edit order with id... view
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def orders_remove(request):
    """
    Remove order with id...
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def orders_fullfill(request):
    """
    Fullfill order with ID and set its state to 'fulfilled'
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def deliverymethod_list(request):
    """
    Show delivery methods with their prices
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def deliverymethod_add(request):
    """
    Add delivery methods
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def deliverymethod_edit(request):
    """
    Edit delivery methods
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def deliverymethod_remove(request):
    """
    Remove delivery methods
    :param request:
    :return:
    """
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass

@staff_member_required
def contractor_add(request):
    pass

@staff_member_required
def contractor_edit(request):
    pass

@staff_member_required
def contractor_remove(request):
    pass

@staff_member_required
def contractor_list(request):
    pass

@login_required
@staff_member_required
def deliveryaddress_add(request):
    pass

@staff_member_required
def deliveryaddress_edit(request):
    pass

@staff_member_required
def deliveryaddress_remove(request):
    pass

@staff_member_required
def deliveryaddress_list(request):
    pass