
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseForbidden, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from activities.models import Activity
from api import ActivitySerializer


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


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def activity_list(request):
    """List all activities, or create activity."""
    if request.method == 'GET':
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
