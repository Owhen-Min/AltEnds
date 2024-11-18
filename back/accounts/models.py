import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    primary_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField(max_length=20, default='익명')
    email = models.EmailField(max_length=254)
    profile_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    join_date = models.DateField(auto_now_add=True)
    token = models.IntegerField(default=100)    
