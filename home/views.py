

from django.shortcuts import render,redirect
from django.views import View
from .models import *

class HomeView(View):
    views={}


class BaseView(HomeView):
    def get(self, request, *args, **kwargs):
        self.views['categories']=Category.objects.filter(status='active')
        self.views['sliders']=Slider.objects.filter(status='active')
        self.views['brands']=Brand.objects.filter(status='active')
        self.views['hots']=Item.objects.filter(status='active', label='hot')
        self.views['new']=Item.objects.filter(status='active', label='new')
        self.views['ads']=Ad.objects.all()

        return render(request,'index.html', self.views)

class CategoryItemView(BaseView):
    def get(self, request, slug):
        category_item=Category.objects.get(slug=slug).id
        self.views['category_items']=Item.objects.filter(category=category_item)
        return render(request, 'category.html', self.views)

class ItemSearchView(BaseView):
    def get(self, request, ):
        search = request.GET.get('search', None)

        if search is None:
            return redirect('home:/')
        else:
            self.views['search_items']=Item.objects.filter(name__icontains=search)
            return render(request, 'search.html',self.views)
        return render(request,'search.html')

class ProductListView(BaseView):
    def get(self, request):
        self.views['items']=Item.objects.filter(status='active')
        return render(request, 'product-list.html', self.views)

class ProductDetailsView(BaseView):
    def get(self, request, slug):
        self.views['details']=Item.objects.filter(slug=slug)
        return render(request, 'product-detail', self.views)



