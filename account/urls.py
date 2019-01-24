from django.urls import path, reverse_lazy
from django.conf.urls import url
from account.views import index, Cadastro
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordResetView, PasswordChangeDoneView,
    PasswordChangeView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView

)

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    
    path('password_change/', 
        PasswordChangeView.as_view(template_name='account/password_change_form.html'),
        name='password_change'),
    path('password_change/done/',
        PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
        name='password_change_done'),
    path('password_reset/',
        PasswordResetView.as_view(template_name='account/password_reset_form.html'),
        name='password_reset'),
    path('password_reset/done/',
        PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('reset/done/',
        PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
        name='password_reset_complete'),
]

