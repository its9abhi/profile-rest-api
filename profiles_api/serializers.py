from rest_framework import serializers
from profiles_api import models

class HelloSerializers(serializers.Serializer):
    """Serializers a name field for testing APIView"""
    name =serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    """Serializer for a user profile objects"""
    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
        'password':{'write_only':True,'style':{'input_type':'password'}}
        }

    def create(self,validated_data):
        """create and return a new user"""
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

    def update(self,instance,validated_data):
        """handle updating user account"""
        if 'password' in validated_data:
            password=validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance,validated_data)
