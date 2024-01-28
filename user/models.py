from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=1000, default='Johnson Masino')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Custom User'

    # USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    username = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    sex = models.CharField(max_length=1, default='M', blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    
    class Meta:
        ordering = ['-created_at']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

# This is a chat model
class Chat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField(max_length=1000)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Message'


    def __str__(self):
        return f"{self.sender} - {self.receiver}"
    
    @property
    def sender_username(self):
        sender_username = User.objects.get(username = self.sender)
        return sender_username
    
    @property
    def receiver_username(self):
        receiver_username = User.objects.get(username = self.receiver)
        return receiver_username

    