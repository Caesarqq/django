from rest_framework import serializers
from .models import Mobiletechnic


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobiletechnic
        fields = ('title', 'cat_id')