from django.shortcuts import render
from django.http import HttpResponse

from reviews.models import Product,Review

# Create your views here.

def index(request):
	product_list=Product.objects.all()
	context={'product_list':product_list}
	return render(request,'reviews/index.html',context)


def detail(request,product_id):
	p=Product.objects.get(id=product_id)
	reviews_list=p.review_set.all()
	context={'p':p,'reviews_list':reviews_list}
	return render(request,'reviews/product_detail.html',context)
