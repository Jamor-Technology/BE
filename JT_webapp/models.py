from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class testimonies(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=300) 
    role = models.CharField(max_length=300)
    profile_picture = models.ImageField
    story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return self.username
