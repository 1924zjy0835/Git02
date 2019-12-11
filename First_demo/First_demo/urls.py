"""First_demo URL Configuration

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
from book import views
from django.urls import path,include

urlpatterns = [
    # 空白字符匹配的是http://127.0.0.1:8000
    path('', views.index,name = 'index'),
    # 主url只要能够匹配规则book/就会找到相对应的book下的urls.py这个文件中的视图函数。
    # 并且include()函数中的urls传递的值是相对于当前的这个项目来说的。此处传递的就是book.urls,
    # 在浏览器或者是客户端传来的参数请求能够匹配到此处的主url时，就会转到book.urls。
    #  查找并且匹配相对应的次url,如果可以匹配到相对应的次url，就会执行相对应的视图函数。
    path('book/', include('book.urls')),
]
