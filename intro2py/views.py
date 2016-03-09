
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        user = None
        try:
            user = User.objects.create_user(
                request.POST.get('username'), '1234')
        except IntegrityError:
            return HttpResponseForbidden('User already registered!')
        return JsonResponse({'username': user.username, 'pk': user.pk})
    return HttpResponseForbidden()
