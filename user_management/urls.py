from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "user_management"
urlpatterns = [
    path('home/', views.user_home, name='user'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login')

]
