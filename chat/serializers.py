from rest_framework import serializers
from user.models import User, Chat

class ChatSerializer(serializers.ModelSerializer):
    receiver_username = serializers.ReadOnlyField(source='receiver.username')
    sender_username = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Chat
        fields = ['id', 'user', 'sender', 'sender_username', 'receiver', 'receiver_username', 'message', 'is_read', 'created_at']
        read_only_fields = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user', 'full_name', 'username', 'email']
        read_only_fields = ['id']