from django.shortcuts import render
from django.http import HttpResponse

def book(request):
    return HttpResponse("图书列表")
