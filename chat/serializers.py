from rest_framework import serializers
from user.models import User, Chat
from user.serializers import UserSerializer

class ChatSerializer(serializers.ModelSerializer):
    receiver_username = serializers.ReadOnlyField(source='receiver.username')
    sender_username = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Chat
        fields = ['id', 'user', 'sender', 'sender_username', 'receiver', 'receiver_username', 'message', 'is_read', 'created_at']
        read_only_fields = ['id', 'is_read', 'created_at']
        extra_kwargs = {
            'sender': {'read_only': True},
            'receiver': {'read_only': True}
        }
