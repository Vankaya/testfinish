from  rest_framework import serializers
from  .models import Messages


class MessegesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Messages
        fields=('email', 'body')
