
from django.urls import path
from news import views



urlpatterns = [
    
    path('', views.home,name="home" ),
    path('categories',views.categories,name="categories" ),
    path('about',views.aboutx,name="about" )
    
    
    ]
    


    