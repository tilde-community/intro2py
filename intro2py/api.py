
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
        fields = ('pk', 'when', 'text', 'kind')


class ActivityViewSet(viewsets.ModelViewSet):
    # filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    # filter_fields = ('kind', 'text', 'when')
    # ordering_fields = '__all__'
    # queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = Activity.objects.all()
        pk__gt = self.request.query_params.get('pk__gt', None)
        text = self.request.query_params.get('text', None)
        kind = self.request.query_params.get('kind', None)
        top = self.request.query_params.get('top', None)
        bottom = self.request.query_params.get('bottom', None)
        print pk__gt, top, bottom
        if filters is not None:
            queryset = queryset.filter(pk__gt=int(pk__gt))
        if text:
            queryset = queryset.filter(text__icontains=text)
        if kind:
            queryset = queryset.filter(kind__icontains=kind)
        return queryset[top: bottom]


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
router.register(r'activities', ActivityViewSet, base_name='activities')
