from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse('Hello world!')


async def a_index(request: HttpRequest):
    return HttpResponse('Async Hello world!')
