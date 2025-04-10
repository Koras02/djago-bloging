from django.db import models

class Product(models.Model):
     name = models.CharField(max_length=100) # Product Name 
     price = models.DecimalField(max_digits=10, decimal_places=2) # Product Price 
     stock = models.IntegerField() # product stock
     
     def __str__(self):
        return self.name # Product name 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) # Title
    content = models.TextField()   # SubScribe
    create_at = models.DateTimeField(auto_now_add=True) # create Date  
    updated_at = models.DateTimeField(auto_now=True) # update Date
    
    def __str__(self):
        return self.title 