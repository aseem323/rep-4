from django.urls import path, include
from application.views import test,function1,func2
urlpatterns = [
path("",test),
path("home",function1),
path("home1",func2),
    
]
  