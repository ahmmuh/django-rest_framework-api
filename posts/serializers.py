from rest_framework import serializers
from . models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post