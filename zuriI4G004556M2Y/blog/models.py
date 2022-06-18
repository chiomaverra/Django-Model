from django.db import models
from django.contrib.auth import get_user_model
user= get_user_model()
# Create your models here.
class post(models.Model):
    Title= models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(user, on_delete= models.CASCADE, related_name='blog_post')
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField(default= 'timezone.now')