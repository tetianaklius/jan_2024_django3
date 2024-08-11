from django.urls import path

from apps.users.views import UserBlockView, UserListCreateView, UserToAdminView, UserUnBlockView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/unblock', UserUnBlockView.as_view()),
    path('/<int:pk>/admins', UserToAdminView.as_view()),
]