from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.dataclasses.user_dataclass import User
from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoverToken

from apps.auth.serializers import EmailSerializer, PasswordSerializer
# from apps.auth.serializers import ResetPasswordSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def patch(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecoveryPasswordRequestView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_email(user=user)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)  # password
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user: User = JWTService.verify_token(token, RecoverToken)
        user.set_password(serializer.data['password'])
        user.save()
        EmailService.recovery_confirm_email(user)
        return Response({'success': 'Your password is changed successfully!'}, status=status.HTTP_200_OK)
