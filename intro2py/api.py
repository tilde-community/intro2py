
from rest_framework import routers, serializers, viewsets

from questions.models import Question


# Serializers define the API representation.
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('body',)


# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
