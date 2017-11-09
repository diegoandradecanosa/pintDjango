from django.conf.urls import include, url
from reviews import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^(?P<product_id>\d+)/$',views.detail,name='detail'),
]
