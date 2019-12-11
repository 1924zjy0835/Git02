from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎来到首页")

def book(request):
    return HttpResponse("图书列表")

def movie(request):
    return HttpResponse("电影首页")
