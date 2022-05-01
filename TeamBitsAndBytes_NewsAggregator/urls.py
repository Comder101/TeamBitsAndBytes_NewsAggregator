from django.contrib import admin
from django.urls import path,include
from news import views
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    
    
    ]
    

