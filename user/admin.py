from django.contrib import admin
from .models import User, Chat

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

class ChatAdmin(admin.ModelAdmin):
    list_editable = ['is_read']
    list_display = ['sender', 'receiver', 'message', 'is_read']

admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)
