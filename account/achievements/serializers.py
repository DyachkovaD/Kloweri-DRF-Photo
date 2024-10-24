from rest_framework import serializers

from achievements.models import AccountPhoto


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountPhoto
        fields = ['user_id', 'image']
