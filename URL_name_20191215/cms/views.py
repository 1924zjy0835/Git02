from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse('哈喽，这是后台首页')
    else:
        # 获取当前的命名空间
        current_namespace = request.resolver_match.namespace
        return redirect("%s:login" % current_namespace)


def login(request):
    return HttpResponse("嗨喽这是后台登录页面")