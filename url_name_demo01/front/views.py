from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("前台首页")
    else:
        return redirect(reverse('front:login'))


def login(request):
    return HttpResponse("前台登录页面")