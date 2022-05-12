from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register,name="register"),  # ← new entry
    path('login/',auth_views.LoginView.as_view(template_name='core/authentication/login.html')),
    path('logout/',auth_views.LogoutView.as_view(template_name='core/authentication/logout.html')),
    path('verify/', views.verify_code),  # ← new
]
