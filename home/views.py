from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.

class HomeView(View):
    views={}

class BaseView(HomeView):
    def get(self, request):
        self.views['category']=Category.objects.filter(status='active')
        self.views['slider']=Category.objects.filter(status='active')
        self.views['brand']=Brand.objects.filter(status='active')
        self.views['hot']=Item.objects.filter(status='active', label='hot')
        self.views['new']=Item.objects.filter(status='active', label='new')
        self.views['ad']=Ad.objects.all()

        return render(request,'index.html', self.views)


# def home(request, *args):
#     return render(request,'index.html')

