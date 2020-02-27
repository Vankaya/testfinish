from django.urls import path
from .views import MesegeView, PostMessageView

app_name = "messages"

urlpatterns = [
    path('messages/list/<int:page>', MesegeView.as_view()),
    path('messages', PostMessageView.as_view())
]