from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255) 
    pub_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    
    