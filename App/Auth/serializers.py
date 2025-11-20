from wsgiref import validate
from itsdangerous import Serializer
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    """ manipulate create function """
    def create(self, validate_data):
        user = User.objects.create_user(
            username = validate_data["username"],
            password = validate_data["password"]
        )

        return user
