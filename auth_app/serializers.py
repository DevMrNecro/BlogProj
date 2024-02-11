from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def validate(self, data):
        """
        Validate the data to ensure either username or email is provided.
        """
        if 'username' not in data and 'email' not in data:
            raise serializers.ValidationError("Either username or email is required.")
        return data
    
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        # Ensure email is case-insensitive
        email = email.lower() if email else None

        if email:
            # Check if the user with the provided email already exists
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError("User with this email already exists.")
            user = User.objects.create_user(email=email, password=password)
        else:
            # Check if the user with the provided username already exists
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError("User with this username already exists.")
            user = User.objects.create_user(username=username, password=password)

        return user