from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username = username,
            email = email,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.premium = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    premium = models.BooleanField(default=False)
    objects = CustomUserManager()

class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=200)
    url_short = models.CharField(max_length=100, default='j')
    visits = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField('date last modified')
    def __str__(self):
        return self.url
    
    def test_unique_short(self):
        if Url.objects.filter(url_short=self.url_short).exists():
            return False
        else:
            return True

# custom user manager
