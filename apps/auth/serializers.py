from rest_framework import serializers

from apps.users.views import UserModel


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('password',)


