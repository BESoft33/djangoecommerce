from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name='home'

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('search/', ItemSearchView.as_view(), name='search'),
    path('products/', ProductListView.as_view(), name='products'),
    path('details/<slug>', ProductDetailsView.as_view(), name='details'),
    path('category/<slug>', CategoryItemView.as_view(), name='category'),
]

