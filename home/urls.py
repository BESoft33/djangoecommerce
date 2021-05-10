from django.urls import path
from django.views.generic import TemplateView
# from .views import HomeView
from .views import BaseView
app_name='home'

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    #path('',home,)
]
