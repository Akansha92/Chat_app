from django.contrib import admin
from django.urls import path
from chat_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("", views.chat_view, name="home"),  # Root URL redirects to chat page after login
    path("chat/", views.chat_view, name="chat"),
]
