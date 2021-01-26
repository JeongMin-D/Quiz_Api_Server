from rest_framework import serializers
from .models import Multiple_easy, OX_easy, Test_easy
from .models import Multiple_normal, OX_normal, Test_normal
from .models import Multiple_hard, OX_hard, Test_hard


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multiple_easy
        fields = ('title', 'body', 'answer')