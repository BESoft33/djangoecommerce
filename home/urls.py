from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView
# from .views import home
app_name='home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('',home,)
]
