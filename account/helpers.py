from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import permissions


def send_confirmation_email(user):
    context = {
        'small_text_detail':"""
        Thank you for creating an account. Please verify your email
        """,
        'email': user.email,
        'activation_code': user.activation_code
    }
    msg_html = render_to_string('email.html', context)
    plain_message = strip_tags(msg_html)
    subject = 'Acccount activation'
    to_emails = user.email
    mail.send_mail(
        subject,
        plain_message,
        'nelson.mandela.99.99@gmail.com',
        [to_emails],
        html_message=msg_html
    )


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id