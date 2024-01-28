from django.urls import path
from .views import MyChatView

# All urls for chat app(messaging)
urlpatterns = [
    path('chats/<user_id>/', MyChatView.as_view(), name='chats'),
]