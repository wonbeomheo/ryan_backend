from .models import User
from rest_framework.serializers import (
    EmailField,
    CharField,
    Serializer,
    ModelSerializer,
    ValidationError,
)
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer
)
from rest_framework_simplejwt.exceptions import (
    InvalidToken
)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


class UserRegistrationSerializer(ModelSerializer):
    
    password2 = CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "password2"]
        extra_kwargs = {
            "name": {"required": True},
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }
        
    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']
        
        if password != password2:
            raise ValidationError({"password": "Passwords do not match."})
        
        del validated_data['password2']
        
        user = User.objects.create_user(**validated_data)
        return user
        
        
class UserLoginSerializer(Serializer):
    email = EmailField()
    password = CharField(style={"input-type": "password"}, write_only=True)


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None
    
    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            return InvalidToken("No valid token found in cookie 'refresh'") 