from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

from django.utils.functional import lazy

from datetime import datetime

from django.utils.translation import gettext_lazy as _


class OverrodeUserManager(BaseUserManager):
    def create_user(self, email, password):
        email = self.normalize_email(email)

        date_joined = datetime.now()

        user = self.model(email=email, date_joined=date_joined)
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser):
    first_name = models.TextField()
    surname = models.TextField()

    email = models.EmailField(unique=True)

    password = models.CharField(_('password'), max_length=128, null=True)

    images = models.TextField()

    date_joined = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    objects = OverrodeUserManager()

    def __str__(self):
        return f"User #{self._get_pk_val()} with email '{self.email}'"
