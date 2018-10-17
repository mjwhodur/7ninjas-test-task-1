"""
    Module: panel.urls

    Purpose:

        This is a url dispatch module which performs verification of URLs passed to application and applies
        proper views

"""
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^products/remove/(?P<index>[0-9]+)$', views.product_remove, name='product-remove'),
    url(r'^products/edit/(?P<index>[0-9]+)$', views.product_edit, name='product-edit'),
    url(r'^products/view/(?P<index>[0-9]+)$', views.product_view, name='product-view'),
    url(r'^products/add$', views.product_add, name='product-add'),
    url(r'^products$', views.product_list, name='product-list'),
    url(r'^contractors$', views.panel_login, name='contractor-panel'),
    url(r'^order/(?P<index>[0-9]+)/remove$', views.order_remove, name='order-remove'),
    url(r'^order/(?P<index>[0-9]+)/edit$', views.order_edit, name='order-edit'),
    url(r'^order/add$', views.order_add, name='order-add'),
    url(r'^order/(?P<index>[0-9]+)/$', views.panel_login, name='order-view'),
    url(r'^order$', views.order_list, name='orders-list'),
    url(r'^categories/view/(?P<index>[0-9]+)$', views.category_view, name='category-view'),
    url(r'^categories/remove/(?P<index>[0-9]+)$', views.category_remove, name='category-remove'),
    url(r'^categories/edit/(?P<index>[0-9]+)$', views.category_edit, name='category-edit'),
    url(r'^categories/add$', views.category_add, name='category-add'),
    url(r'^categories$', views.category_list, name='categories'),
    url(r'^deliverymethods/view/(?P<index>[0-9]+)$', views.delivery_method_view, name='deliverymethods-view'),
    url(r'^deliverymethods/remove/(?P<index>[0-9]+)$', views.delivery_method_remove, name='deliverymethods-remove'),
    url(r'^deliverymethods/edit/(?P<index>[0-9]+)$', views.delivery_method_edit, name='deliverymethods-edit'),
    url(r'^deliverymethods/add$', views.delivery_method_add, name='deliverymethods-add'),
    url(r'^deliverymethods/$', views.delivery_method_list, name='deliverymethods-list'),
    url(r'^$', views.panel_login, name='panel_default'),
]
