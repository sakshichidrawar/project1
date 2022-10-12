from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse(' I am learning django')

def learn_python(request):
    return HttpResponse(' I am learning python')

def learn_mysql(request):
    return HttpResponse(' I am learning sql')
