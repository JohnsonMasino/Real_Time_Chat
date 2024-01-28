from django.urls import path
from .views import MyChatView, MyChatView2, SendMessageView, ProfileDetailView, SearchUsersView

# All urls for chat app(messaging)
urlpatterns = [
    path('chats/<user_id>/', MyChatView.as_view()),
    path('chats-message/<sender_id>-<receiver_id>/', MyChatView2.as_view()),
    path('send-message/', SendMessageView.as_view()),
    path('profile/<int:pk>/', ProfileDetailView.as_view()),
    path('search/<str:username>/', SearchUsersView.as_view()),
]