from django.urls import include,path
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'reviews/', include('reviews.urls')),    
]
