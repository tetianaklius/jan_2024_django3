from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import ActivateUserView, ResetPasswordView, RestorePasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    #################
    path('/restore_password', RestorePasswordView.as_view()),
    path('/restore_password/<str:token>', ResetPasswordView.as_view()),

]
