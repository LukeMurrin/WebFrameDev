from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom manager for the User model
class CustomUserManager(BaseUserManager):
    # Method for creating a regular user
    def create_user(self, username, email=None, password=None, role='Customer', **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields['role'] = role  # Set the role
        return self._create_user(username, email, password, **extra_fields)

    # Method for creating a superuser
    def create_superuser(self, username, email=None, password=None, role='Admin', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields['role'] = role  # Set the role

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

    # Helper method for creating a user
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

# Custom User model with additional fields
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
        ('Logistics Manager', 'Logistics Manager'),
        ('Advertiser', 'Advertiser'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Customer')  # Role field for user roles

    # Override default related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )

    objects = CustomUserManager()  # Use the custom manager

    def __str__(self):
        return self.username  # String representation of the user