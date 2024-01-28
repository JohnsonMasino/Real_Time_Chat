from user.models import User, Chat, Profile
from .serializers import ChatSerializer, ProfileSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from django.db.models import Q, Subquery, OuterRef
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# This is to get all messages sent to a user from many users
class MyChatView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user_id = self.kwargs['user_id']
    
        messages = Chat.objects.filter(
            id__in=Subquery(
                User.objects.filter(
                    Q(sender__receiver=user_id) |
                    Q(receiver__sender=user_id)
                ).distinct().annotate(
                    last_message_id=Subquery(
                        Chat.objects.filter(
                            Q(sender=OuterRef('id'), receiver=user_id) |
                            Q(receiver=OuterRef('id'), sender=user_id)
                        ).order_by('-id')[:1].values_list('id', flat=True)
                    )
                ).values_list('last_message_id', flat=True).order_by('-id')
            )
        ).order_by('-id')
        return messages
    
# This is to get all messages sent to a user from a particular user
class MyChatView2(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        receiver_id = self.kwargs['receiver_id']

        messages = Chat.objects.filter(
            sender__in=[sender_id, receiver_id],
            receiver__in=[sender_id, receiver_id]
        )
        return messages
    
# This is to send a message to a user
class SendMessageView(CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

# This the profile details of a user
class ProfileDetailView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    
# This is to search all users
class SearchUsersView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        username = self.kwargs['username']
        logged_in_user = self.request.user
        users = Profile.objects.filter(
            Q(user__username__icontains=username) |
            Q(full_name__icontains=username) |
            Q(email__icontains=username) &
            ~Q(user=logged_in_user)
        )
        if not users.exists():
            return Response(
                {'detail': 'No user found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
