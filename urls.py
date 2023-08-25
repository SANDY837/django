from django.urls import path
from sandeep import views
urlpatterns = [
    path('home',views.home,name='sandeep-sandy'),
    path('about',views.about,name='sandeep-about'),
]