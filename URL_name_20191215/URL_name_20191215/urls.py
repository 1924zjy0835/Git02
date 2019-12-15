"""URL_name_20191215 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from movie import views

urlpatterns = [
    path('', include('front.urls')),
    # 同一个APP下面有两个实例
    path('cms1/', include(('cms.urls','cms'),namespace='cms1')),
    path('cms2/', include(('cms.urls','cms'),namespace='cms2')),
    path('movie/',include([
        path('',views.movie),
        path('list/',views.movie_list),
    ]))
]
