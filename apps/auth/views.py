from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService

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


#######################################################
class RestorePasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data['email']
        user = EmailService.check_email(email=email)

        if user:
            token = JWTService.create_token(user, ActivateToken)
            EmailService.send_token(email, token)
            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User with credentials not found"}, status=status.HTTP_404_NOT_FOUND)


class ResetPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def patch(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, ActivateToken)
        user.set_password(kwargs['password'])
        user.save()
        EmailService.send_password_ok(user.email)




