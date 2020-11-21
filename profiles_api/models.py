from django.db import models
from django.contrib.auth.models import AbstactBaseUser
from django.contrib.auth.models import PermissionMixin


class UserProfile (AbstractBaseUser, PermissionMixin):
    """Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
