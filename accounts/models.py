from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email):
        User.objects.create(email=email)

    def create_superuser(self, email, password):
        self.create_user(email=email)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()


class Token(models.Model):
    email = models.EmailField()
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
