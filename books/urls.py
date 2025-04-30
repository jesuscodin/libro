from django.urls import path
from .import views

app_name = 'books'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('browse/', views.browse, name='browse'),
    path('explore/',views.explore, name='explore'),
    path('about/', views.about, name='about'),
]