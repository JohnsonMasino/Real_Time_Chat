from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Customised User'

    # USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    

# This is a chat model
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
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

    
    