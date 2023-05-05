from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.title
    

class Image(models.Model):
   
    image = models.ImageField(upload_to='images/')
    

   
    


