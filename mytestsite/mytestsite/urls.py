"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from trips.views import find_similarity, get_places, home
#, recommend_list

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^find_similarity/$', find_similarity),
	url(r'^home/$', home),
    #url(r'^u/$',recommend_list),
    url(r'^api/get_places/', get_places),
]
