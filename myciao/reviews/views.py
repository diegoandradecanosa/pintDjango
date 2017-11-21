from django.http import HttpResponse
from reviews.models import Product,Review
from reviews.forms import NewProductForm, NewReviewForm, LoginForm, SignupForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    return render(request, 'reviews/signup.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect(request.GET['next'])

def index(request):
	loginError=""

	if 'name' in request.POST:
		name=request.POST['name']
		barcode=request.POST['barcode']
		p=Product(name=name,barcode=barcode)
		p.save()
	if 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)		
		if user is not None:
			login(request, user)	
		else:
			loginError="Error de login"			

	product_list=Product.objects.all()
	newProductForm=NewProductForm()
	loginForm=LoginForm()
	signupForm=SignupForm()
	
	

	if request.user.is_authenticated:
		context={'product_list':product_list,'new_product_form':newProductForm,'user':request.user,'login_form':loginForm,'signup_form':signupForm,'loginError':loginError}
	else:
		context={'product_list':product_list,'new_product_form':newProductForm,'login_form':loginForm,'signup_form':signupForm,'loginError':loginError}
	
	
	return render(request,'reviews/index.html',context)


def detail(request,product_id):
	p=Product.objects.get(id=product_id)
	reviews_list=p.review_set.all()
	loginError=""

	if 'title' in request.POST:
		title=request.POST['title']
		text=request.POST['text']
		p.review_set.create(title=title,text=text)
	if 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)	
		if user is not None:
			login(request, user)	
		else:
			loginError="Error de login"

	newReviewForm=NewReviewForm()		
	newReviewForm.helper.form_action = reverse('detail', kwargs={'product_id': p.id})		
	loginForm=LoginForm()
	signupForm=SignupForm()



	if request.user.is_authenticated:
		context={'p':p,'reviews_list':reviews_list,'new_review_form':newReviewForm,'user':request.user,'login_form':loginForm,'signup_form':signupForm,'loginError':loginError}
	else:
		context={'p':p,'reviews_list':reviews_list,'new_review_form':newReviewForm,'login_form':loginForm,'signup_form':signupForm,'loginError':loginError}


	return render(request,'reviews/product_detail.html',context)
