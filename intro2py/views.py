
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseForbidden


def register_user(request):
    if request.method == 'POST':
        try:
            User.objects.create_user(request.POST.get('username'), '1234')
        except IntegrityError:
            raise HttpResponseForbidden('User already registered!')
