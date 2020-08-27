from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model 
User = get_user_model()
from rest_framework import serializers
from .models import ConsumerProfile, UserAccount

class ConsumerProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model = ConsumerProfile

class UserCreateSerializerNew(UserCreateSerializer):
    consumer_profile = ConsumerProfileSerializer(required=True)
    class meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password', 'consumer_profile')
   
    def perform_create(self, validated_data):
        print('poasd')
        consumer_profile_serializer = validated_data.pop('consumer_profile')
        user_account = User.objects.create_user(**validated_data)
        user_profile = ConsumerProfile.objects.create(**consumer_profile_serializer, name=consumer_profile_serializer['name'], account=user_account)
        print('passe')
        return user_account