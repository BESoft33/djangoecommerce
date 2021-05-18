from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name='usermanager'

urlpatterns = [
    path('login', login, name='login'),
    # path('signup', signup, name='signup'),


]