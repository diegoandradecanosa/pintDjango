from django.shortcuts import render
from django.http import HttpResponse

from reviews.models import Product,Review

# Create your views here.

def index(request):
	product_list=Product.objects.all()
	output=''
	for p in product_list:
		output=output+'<a href=\"'+str(p.id)+'\">'+p.name+"</a><BR>"
	return HttpResponse(output)

def detail(request,product_id):
	p=Product.objects.get(id=product_id)
	output=p.name+'<BR><BR>'
	reviews_list=p.review_set.all()
	for r in reviews_list:
		output=output+r.title+'<BR>'+r.text+'<BR><BR>'
	return HttpResponse(output)
