from django.contrib import admin
from .models import User, Chat, Profile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

class ChatAdmin(admin.ModelAdmin):
    list_editable = ['is_read']
    list_display = ['sender', 'receiver', 'message', 'is_read']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'sex', 'phone_number','country', 'state',
                    'created_at', 'is_active']

admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Profile, ProfileAdmin)
