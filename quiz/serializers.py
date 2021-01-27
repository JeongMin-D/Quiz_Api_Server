from rest_framework import serializers
from .models import OX_law, OX_safety, OX_service, OX_transit
from .models import Law_easy, Law_normal, Law_hard, Transit_easy, Transit_normal, Transit_hard
from .models import Safety_easy, Safety_normal, Safety_hard, Service_easy, Service_normal, Service_hard
from .models import Practice, Challenge


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = OX_law
        fields = ('title', 'body', 'answer')