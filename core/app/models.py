from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class OverrodeUserManager(BaseUserManager):
    def create_user(self, email, password):
        email = self.normalize_email(email)

        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    objects = OverrodeUserManager()
