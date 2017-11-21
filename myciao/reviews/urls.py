from django.conf.urls import include, url
from reviews import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^(?P<product_id>\d+)/$',views.detail,name='detail'),
	url(r'^logout/$', views.logout_view, name='logout_view'),
	url(r'^signup/$', views.signup_view, name='signup_view'),
]
