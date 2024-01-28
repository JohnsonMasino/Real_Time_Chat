from django.urls import path
from .views import MyChatView

urlpatterns = [
    path('chats/<user_id>/', MyChatView.as_view(), name='chats'),
]