"""ninja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import exchange.urls
import panel.urls
from django.conf.urls import url, include
#from django.contrib.sites import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^api/', include(exchange.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token, name='JWT-Update'),
    url(r'^api-token-github/', obtain_jwt_token, name='Oauth2-GitHub'),
    url(r'^api-token-twitter/', obtain_jwt_token, name='Oauth2-Twitter'),
    url(r'^api-token-refresh/', refresh_jwt_token, name='JWT-Refresh'),
    url(r'^api-token-verify/', verify_jwt_token, name='JWT-Verify'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^panel/', include(panel.urls)),
    url(r'^$', views.DefaultView, name='home')
]
