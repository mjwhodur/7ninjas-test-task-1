from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(), name='api-product-list'),
    url(r'^products/(?P<pk>[0-9]+)$', views.ProductDetail.as_view(), name='product-detail'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='api-product-detail2'),
    url(r'^products/(?P<pk>[0-9]+)/like$', views.ProductLike, name='api-product-likes'),
    url(r'^products/(?P<pk>[0-9]+)/like/$', views.ProductLike, name='api-product-likes2'),
    url(r'^order/', views.PlaceOrder.as_view(), name='api-place-order'),
    url(r'^categories/$', views.CategoryList.as_view(), name='category-list'),
    url(r'^categories/byName/(?P<Title>.+)$', views.CategoryDetailByName.as_view()),
    url(r'^categories/byName/$', views.CategoryDetailByNameDescription.as_view(), name='category-detail-by-name'),
    url(r'^categories/(?P<pk>[0-9]+)$', views.CategoryDetail.as_view(), name='category-detail'),
    url(r'^view/$', views.api_root, name='home'),
    url(r'^', views.api_root, name='api-root'),

    #
]

urlpatterns = format_suffix_patterns(urlpatterns)
