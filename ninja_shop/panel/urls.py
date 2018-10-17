"""
    Module: panel.urls

    Purpose:

        This is a url dispatch module which performs verification of URLs passed to application and applies
        proper views

"""
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^products/remove/(?P<index>[0-9]+)$', views.panel_login, name='product-remove'),
    url(r'^products/edit/(?P<index>[0-9]+)$', views.panel_login, name='product-edit'),
    url(r'^products/view/(?P<index>[0-9]+)$', views.panel_login, name='product-view'),
    url(r'^products/add$', views.panel_login, name='product-add'),
    url(r'^products$', views.panel_login, name='product-list'),
    url(r'^contractors$', views.panel_login, name='contractor-panel'),
    url(r'^order/(?P<index>[0-9]+)/remove$', views.panel_login, name='order-remove'),
    url(r'^order/(?P<index>[0-9]+)/edit$', views.panel_login, name='order-edit'),
    url(r'^order/add$', views.panel_login, name='order-add'),
    url(r'^order/(?P<index>[0-9]+)/$', views.panel_login, name='order-view'),
    url(r'^order$', views.panel_login, name='orders-list'),
    url(r'^categories/view/(?P<index>[0-9]+)$', views.panel_login, name='category-view'),
    url(r'^categories/remove/(?P<index>[0-9]+)$', views.panel_login, name='category-remove'),
    url(r'^categories/edit/(?P<index>[0-9]+)$', views.panel_login, name='category-edit'),
    url(r'^categories/add$', views.panel_login, name='category-add'),
    url(r'^categories$', views.panel_login, name='categories'),
    url(r'^deliverymethods/view/(?P<index>[0-9]+)$', views.panel_login, name='deliverymethods-view'),
    url(r'^deliverymethods/remove/(?P<index>[0-9]+)$', views.panel_login, name='deliverymethods-remove'),
    url(r'^deliverymethods/edit/(?P<index>[0-9]+)$', views.panel_login, name='deliverymethods-edit'),
    url(r'^deliverymethods/add$', views.panel_login, name='deliverymethods-add'),
    url(r'^deliverymethods/$', views.panel_login, name='deliverymethods-list'),
    url(r'^$', views.panel_login, name='panel_default'),
]
