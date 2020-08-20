from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.
from ecommerce import settings


class CustomAccountManager(BaseUserManager):
    # parameters are the required fields
    def create_user(self, email, username, name, password=None):

        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not name:
            raise ValueError("Users must have a name")
        # creation of new user
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    # default fields
    email = models.EmailField(verbose_name="email", max_length=70, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # personalized fieds
    name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']  # required field other than email

    objects = CustomAccountManager()

    def __str__(self):
        return self.username + ", " + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
