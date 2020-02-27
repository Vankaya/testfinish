from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from .models import Messages
from  .serializers import  MessegesSerializer


class MesegeView(ListModelMixin, GenericAPIView):
    """
    Get messages list with pagination
    """
    serializer_class = MessegesSerializer

    def get(self, request, *args, **kwargs):
        page_number = self.kwargs.get('page')
        offset = page_number * 10
        self.queryset = Messages.objects.all()[offset:offset+10]

        return self.list(request, *args, **kwargs)

class PostMessageView(CreateModelMixin, GenericAPIView):
    serializer_class = MessegesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)