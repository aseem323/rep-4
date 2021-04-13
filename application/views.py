from django.shortcuts import render
from django.http import HttpResponse
def test(request):
    return HttpResponse("javad php")
def function1(request):
    return render(request,'log-boot.html')
def func2(request):
    return HttpResponse("hello every one")

# Create your views here.
