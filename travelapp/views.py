from django.shortcuts import render
from django.http import HttpResponse
from .models import place
from .models import blogs


# Create your views here.
def fun(request):
   var=place.objects.all()
   blogvar = blogs.objects.all()

   return render(request,"index.html",{'results':var,'blogresults': blogvar})

def index(request):
    return render(request,'index.html')





# def addition(request):
#     num1=int(request.GET['num1'])
#     num2=int(request.GET['num2'])
#     result=num1+num2
#     return render(request,"result.html",{'sum':result})

def addition(request):
    num1=int(request.POST['num1'])
    num2=int(request.POST['num2'])
    result=num1+num2
    return render(request,"result.html",{'sum':result})
