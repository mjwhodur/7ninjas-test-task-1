from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view(), name='api-product-list'),
    #    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='api-product-detail'),
    #    url(r'^products/(?P<pk>[0-9]+)/like/$', views.ProductLike.as_view(), name='api-product-highlight'),
    #    url(r'^likes/', views.Likes.as_view(), name='api-user-likes'),
    url(r'^order/', views.PlaceOrder, name='api-place-order'),
    url(r'^users/', views.UserList, name='user-list'),
    url(r'^view/$', views.api_root),
    #
]

urlpatterns = format_suffix_patterns(urlpatterns)
