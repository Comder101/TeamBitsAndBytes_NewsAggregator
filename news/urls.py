
from django.urls import path
from news import views



urlpatterns = [
    
    path('', views.home,name="home" ),
    path('main',views.main,name="main" ),
    path('about',views.aboutx,name="about" ),
    path('sports',views.categories_sp,name="categories_sp"),
    path('politics',views.categories_po,name="categories_po"),
    path('education',views.categories_edu, name="categories_edu"),
    path('technology',views.categories_tec, name="categories_tec"),
    path('weather',views.categories_wea, name="categories_wea"),
    
    ]
    


    