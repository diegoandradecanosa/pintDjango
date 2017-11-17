from django.shortcuts import render
from django.http import HttpResponse

from reviews.models import Product,Review
from reviews.forms import NewProductForm, NewReviewForm
from django.urls import reverse

# Create your views here.

def index(request):
	if 'name' in request.POST:
		name=request.POST['name']
		barcode=request.POST['barcode']
		p=Product(name=name,barcode=barcode)
		p.save()
	product_list=Product.objects.all()
	newProductForm=NewProductForm()
	context={'product_list':product_list,'new_product_form':newProductForm}
	
	return render(request,'reviews/index.html',context)


def detail(request,product_id):
	p=Product.objects.get(id=product_id)
	reviews_list=p.review_set.all()
	if 'title' in request.POST:
		title=request.POST['title']
		text=request.POST['text']
		p.review_set.create(title=title,text=text)
	newReviewForm=NewReviewForm()		
	newReviewForm.helper.form_action = reverse('detail', kwargs={'product_id': p.id})		
	context={'p':p,'reviews_list':reviews_list,'new_review_form':newReviewForm}
	return render(request,'reviews/product_detail.html',context)
