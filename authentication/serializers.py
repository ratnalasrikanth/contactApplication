from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    password = serializers.CharField(max_length=255,min_length=8,write_only=True)
    email = serializers.EmailField(max_length=255,min_length=8,write_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','username']

    def validate(self,attrs):
        email = attrs.get('eamil','')
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email":"{} is already in use.".format(attrs['email'])})
        
        return super().validate(attrs)

    def create(self,validated_data):
        # return User.objects.create(**validated_data)
        user = User.objects.create_user(username = validated_data['username'],password = validated_data['password'],
                                        first_name=validated_data['first_name'],last_name=validated_data['last_name'],
                                        email=validated_data['email'])
        return user