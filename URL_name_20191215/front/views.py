from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("嗨喽这是前台首页哦！")
    else:
        return redirect(reverse('front:signin'))


def login(request):
    return HttpResponse("前台登录页面")
