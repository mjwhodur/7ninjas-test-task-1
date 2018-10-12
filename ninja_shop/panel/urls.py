from django.conf.urls import url
from . import views

urlpatterns = [
    #   UKŁAD
    #
    #   Kontrahenci
    #       Miejsca dostawy
    #           Dodawanie, edycja, usuwanie
    #
    #   Zamówienia
    #       Podgląd
    #
    #   Produkt
    #       Dodaj, edytuj, usuń, podgląd
    #
    #   Waluty
    #       Dodaj, edytuj, usuń, podgląd
    #
    #   Cennik
    #       Ustaw cenę dla produktu
    #           Automatycznie, ręcznie (podłączy się automatycznie do widoku)
    #
    #   Pseudo-admin
    #       Wypełnij

    url(r'^products/remove/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^products/edit/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^products/view/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^products/add$', views.panel_login),
    url(r'^products/page/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^products$', views.panel_login),
    url(r'^contractors/view/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^contractors/remove/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^deliveryaddress/remove/(?P<deliveryaddress_index>[0-9]+)$', views.panel_login),
    url(r'^deliveryaddress/edit/(?P<deliveryaddress_index>[0-9]+)$', views.panel_login),
    url(r'^contractors/edit/(?P<contractor_index>[0-9]+)/delivery/add$', views.panel_login),
    url(r'^contractors/edit/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^contractors/add$', views.panel_login),
    url(r'^contractors$', views.panel_login),
    url(r'^order/(?P<index>[0-9]+)/remove$', views.panel_login),
    url(r'^order/(?P<index>[0-9]+)/edit$', views.panel_login),
    url(r'^order/add$', views.panel_login),
    url(r'^order/(?P<index>[0-9]+)/$', views.panel_login),
    url(r'^order$', views.panel_login),
    url(r'^categories/view/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^categories/remove/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^categories/edit/(?P<index>[0-9]+)$', views.panel_login),
    url(r'^categories/add$', views.panel_login),
    url(r'^categories$', views.panel_login),
    url(r'^$', views.panel_login, name='panel_default'),
]
