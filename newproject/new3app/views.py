from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style=color:skyblue>welcome to third home page</h1>")
