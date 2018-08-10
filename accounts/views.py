import sys

from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse

from accounts.models import Token

CHECK_EMAIL_MESSAGE = "Check your email, we've sent you a link you can use to log in."


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email],
    )

    messages.success(
        request,
        CHECK_EMAIL_MESSAGE
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')
