from django.db import models
import datetime

# Create your models here.
class list(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='Unknown')
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    body = models.TextField()
    uploaded_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name