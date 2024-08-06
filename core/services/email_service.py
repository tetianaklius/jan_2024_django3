import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.dataclasses.user_dataclass import User
from core.services.jwt_service import ActivateToken, JWTService

from apps.users.models import UserModel


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject='') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject=subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def send_test(cls):
        cls.__send_email('tetianaklius@gmail.com', 'test.html', {}, 'Test Email')

    @classmethod
    def register_email(cls, user: User):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email(
            user.email,
            template_name='registration.html',
            context={'name': user.profile.name, 'url': url},
            subject='Register'
        )

##########################################
    @staticmethod
    def check_email(email: str) -> UserModel | None:
        return UserModel.objects.filter(email=email).first()

    @classmethod
    def send_token(cls, email: str, token: str) -> None:
        url = f'http://localhost:3000/restore_password/{token}'
        cls.__send_email(
            email,
            'token_to_restore.html',
            {'url': url},
            'Restore Password Email')

    @classmethod
    def send_password_ok(cls, email: str) -> None:
        cls.__send_email(
            email,
            'password_confirm.html',
            {},
            'Password Changed Email')


