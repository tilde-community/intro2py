
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseForbidden, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        user = None
        try:
            user = User.objects.create_user(
                request.POST.get('username'), '1234')
        except IntegrityError:
            return HttpResponse(status=403, reason='Username already taken!')
        return JsonResponse({'username': user.username, 'pk': user.pk})
    return HttpResponseForbidden()


@csrf_exempt
def deactivate(request):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.POST.get('username'))
        user.is_active = False
        return HttpResponse(status=200)
    return HttpResponseForbidden()
