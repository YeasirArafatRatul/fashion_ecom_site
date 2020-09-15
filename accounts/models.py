from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, phone, email, password=None, is_active=True, is_staff=False, is_admin=False):
        # all the required fields must be passed as arguments
        if not email:
            raise ValueError("Put an email address")
        if not password:
            raise ValueError("Input a password")
        if not username:
            raise ValueError("You must add your username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.phone = phone
        user.set_password(password)

        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

        # user = user_object

    def create_staffuser(self, username, phone, email, password=None):
        user = self.create_user(
            email,
            username=username,
            email=email,
            phone=phone,
            password=password,

            is_staff=True
        )
        return user

    def create_superuser(self, username, phone, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            phone=phone,
            password=password,

            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.IntegerField(unique=True, null=True, blank=True)
    # for the stuffs
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    # username & password is required by django default
    REQUIRED_FIELDS = ['phone', 'email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_level):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class UserProfileManager(models.Manager):

    def profile_update(self, image):
        profile_update_obj = self.model(image=image)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.email}'

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

    objects = UserProfileManager()

# signal.py


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        post_save.connect(create_profile, sender=User)
