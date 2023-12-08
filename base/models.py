from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200, null=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=400, null=False)
    time = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.text

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.description
