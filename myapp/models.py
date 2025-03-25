from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) # Title
    content = models.TextField()   # SubScribe
    create_at = models.DateTimeField(auto_now_add=True) # create Date  
    updated_at = models.DateTimeField(auto_now=True) # update Date
    
    def __str__(self):
        return self.title 