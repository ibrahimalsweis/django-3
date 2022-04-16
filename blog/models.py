
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, DateField, DateTimeField
# Create your models here.
class Post(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey('Categorys',on_delete=models.CASCADE) 
    title= models.CharField(max_length=60)
    content =models.TextField(max_length=6000)
    date = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='posts/%y/%m/%d')
    def __str__(self):
        return str(self.title)


class Categorys(models.Model):
    
    name=  models.CharField(max_length=50)
    def __str__(self):
        return self.name
