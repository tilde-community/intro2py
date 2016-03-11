
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets, generics, filters

from questions.models import Question
from activities.models import Activity


# Serializers define the API representation.
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'name', 'intro', 'body', 'success_message',
                  'fail_message')


# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('when', 'text', 'kind')


class ActivityViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('kind', 'text', 'when')
    ordering_fields = '__all__'
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityListView(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer = ActivitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('pk', 'kind', 'text')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email')


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('username', 'email')
    ordering = ('username',)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'activities', ActivityViewSet)
