from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager, AbstractBaseUser
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            date_of_birth = date_of_birth
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password):
        user = self.create_user(
            username,
            email,
            password = password,
            date_of_birth = date_of_birth,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
# class CustomUser(AbstractUser):
#     """docstring for CustomUser"""
#     date_of_birth = models.DateTimeField(max_length=50, null=True)
#     def __str__(self):
#         return self.email

class CustomUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name = 'UserName',
        max_length = 255,
        unique = True,
    )
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(
        default='',
        max_length=50,
    )
    last_name = models.CharField(
        default='',
        max_length=50,
    )
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(
        default=timezone.now()
    )

    object = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_level):
        return True

    # @property
    # def is_staff(self):
    #     return self.is_superuser

