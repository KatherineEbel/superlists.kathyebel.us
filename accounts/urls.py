from django.urls import path, include
from accounts import views as account_views

urlpatterns = [
    path('send_login_email', account_views.send_login_email, name='send_login_email'),
    path('login', account_views.login, name='login')
]
