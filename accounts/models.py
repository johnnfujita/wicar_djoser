from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.dispatch import receiver
from django.db.models.signals import post_save

class UserAccountManager(BaseUserManager):
    def create_user(self, email,  password=None, is_superuser=False,is_admin=False, is_staff=False):
        if not email:
            raise ValueError('viiiiixe, be isso ai, ne um email nao')

        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_admin=is_admin, is_superuser=is_superuser)
        
        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email,  password=None):
       
        user_obj = self.create_user(
            email,
          
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
            
        )
        return user_obj



class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    @property
    def consumer_profile(self):
        return self.consumer_profile_set.all()


    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

      

class ConsumerProfile(models.Model):
    # This complement Account (UserAuth class) for the consumers
    account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name="consumer_profile_set")
    name = models.CharField(max_length=120, null=False, blank=False)
    #Define the bucket path
    #user_picture = models.ImageField()
    # Every User will have an address to receive deliveries (it can be overwriten at checkout time)
    #address = models.ForeignKey(NumberLevelAddress, on_delete=models.CASCADE, related_name='consumers')

