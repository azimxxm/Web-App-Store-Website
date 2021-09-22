from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about2/', views.about2, name='about2'),
    path('service/', views.service, name='service'),
    path('products/', views.products, name='products'),
    path('blog/', views.blog, name='blog'),
    path('pricing/', views.pricing, name='pricing'),

]
