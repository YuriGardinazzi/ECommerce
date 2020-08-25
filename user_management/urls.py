from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = "user_management"
urlpatterns = [
    path('home/', views.user_home, name='user'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('account/', views.account_view, name='account'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user_management:password_change_done'),
                                               template_name='registration/password_change.html'),
         name='password_change'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_complete_user.html'),
         name='password_change_done'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done_user.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('user_management:password_reset_complete'),
                                                                                template_name='registration/password_reset_confirm_user.html'),
         name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('user_management:password_reset_done'),
                                                                 template_name='registration/password_reset_form_user.html',
                                                                 email_template_name='registration/password_reset_email_user.html'),
         name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete_user.html'),
         name='password_reset_complete'),

]
