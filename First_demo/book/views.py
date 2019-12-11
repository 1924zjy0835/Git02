from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎来到首页")

def book(request):
    return HttpResponse("图书列表")

def book_detail(request,book_id):
    text = '您获取的图书ID是：%s ' % book_id
    return HttpResponse(text)

def author_detail(request):
    author_id = request.GET.get('id')
    text = "您好，您获得的作者的ID是： %s " % author_id
    return HttpResponse(text)