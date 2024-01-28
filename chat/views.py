from user.models import User, Chat
from .serializers import ChatSerializer
from rest_framework.generics import ListAPIView
from django.db.models import Q, Subquery, OuterRef

# This is to get all messages sent to a user from many users
class MyChatView(ListAPIView):
    serializer_class = ChatSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
    
        messages = Chat.objects.filter(
            id__in=Subquery(
                User.objects.filter(
                    Q(sender__receiver=user_id),
                    Q(receiver__sender=user_id)
                ).distinct().annotate(
                    last_message_id=Subquery(
                        Chat.objects.filter(
                            Q(sender=OuterRef('id'), receiver=user_id),
                            Q(receiver=OuterRef('id'), sender=user_id)
                        ).order_by('-id')[:1].values_list('id', flat=True)
                    )
                ).values_list('last_message_id', flat=True).order_by('-id')
            )
        ).order_by('-id')
        return messages