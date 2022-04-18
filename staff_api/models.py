from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
import random


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name,contact, is_staff, address, position, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,contact= contact, address = address, position= position, is_staff=is_staff)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name,contact, is_staff, address, position, password=None):
        """Create and save a new superuser with given details"""
        user = self.create_user( email, name, contact, is_staff, address, position, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    staff_id = models.IntegerField(primary_key=True, editable=False, default=random.randint(1000,40000), unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    id = 'staff_id'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','contact', 'address', 'is_staff', 'position']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email