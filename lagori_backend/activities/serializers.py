from rest_framework import serializers
from django.conf import settings
from .models import *

class ActivitySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'title', 'date', 'description', 'image']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None