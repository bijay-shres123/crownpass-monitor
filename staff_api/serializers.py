from attr import validate
from staff_api import models
from rest_framework import serializers
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('staff_id', 'email', 'name', 'password','contact','address','position','is_staff')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            contact =validated_data['contact'],
            address = validated_data['address'],
            position = validated_data['position'],
           
            is_staff = validated_data['is_staff'],
        )

        return user
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)