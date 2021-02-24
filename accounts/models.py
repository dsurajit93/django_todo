from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# from django import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField


class MyAccountManager(BaseUserManager):
    def create_user(self, name, email, phone, password=None, photo=None):
        if not name:
            raise ValueError("User must have a name")
        # if not username:
        #     raise ValueError("User must have a username")
        if not email:
            raise ValueError("User must have an email")
        if not phone:
            raise ValueError("User must have a phone number")

        user = self.model(name=name, email=self.normalize_email(email), phone=phone, photo=photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password):
        user = self.create_user(name=name, email=self.normalize_email(
            email), phone=phone, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):

    name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='Email', unique=True, max_length=60)
    phone = models.BigIntegerField(unique=True)
    date_joined = models.DateTimeField(
        verbose_name='Joined Date', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, default='static/images/user.png')

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

