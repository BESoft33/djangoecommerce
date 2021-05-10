from django.db import models

STATUS = (('active','Available'),('inactive','Unavailable'))
LABEL = (('new','New'),('hot','hot'))

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    status =  models.CharField(max_length=200,choices=STATUS)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    status =  models.CharField(max_length=200,choices=STATUS)

    def __str__(self):
        return self.name
    
class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    status = models.CharField(choices=STATUS, max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    price =models.FloatField()
    discounted_price = models.FloatField(default=0)
    label = models.CharField(max_length=200, choices=LABEL,blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, max_length=200)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=200)
    specification = models.TextField(blank=True)
    category = models.ForeignKey(Category, blank=True,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

