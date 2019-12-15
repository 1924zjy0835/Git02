from django.urls import path
from .import views


# 需要把当前的url映射放到一个变量当中
urlpatterns = [
    path("",views.index,name = "index"),
    path("signin/",views.login,name = "login"),
]