from django.urls import path
from django.urls.resolvers import URLPattern
from app import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('product/<slug>',views.ItemDetailView.as_view(),name='product'),
]
