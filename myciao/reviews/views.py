from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return HttpResponse("Hola mundo")

def detail(request, product_id):
	return HttpResponse("Hola mundo "+ product_id)
