from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import OX_law, OX_safety, OX_service, OX_transit
from .models import Law_easy, Law_normal, Law_hard, Transit_easy, Transit_normal, Transit_hard
from .models import Safety_easy, Safety_normal, Safety_hard, Service_easy, Service_normal, Service_hard
from .models import Practice, Challenge
from .serializers import QuizSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')

@api_view(['GET'])
def randomOX_law(request, id):
    totalOX_law = OX_law.objects.all()
    randomOX_law = random.sample(list(totalOX_law), id)
    serializer = QuizSerializer(randomOX_law, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomOX_safety(request, id):
    totalOX_safety = OX_safety.objects.all()
    randomOX_safety = random.sample(list(totalOX_safety), id)
    serializer = QuizSerializer(randomOX_safety, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomOX_service(request, id):
    totalOX_service = OX_service.objects.all()
    randomOX_service = random.sample(list(totalOX_service), id)
    serializer = QuizSerializer(randomOX_service, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomOX_transit(request, id):
    totalOX_transit = OX_transit.objects.all()
    randomOX_transit = random.sample(list(totalOX_transit), id)
    serializer = QuizSerializer(randomOX_transit, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomLaw_easy(request, id):
    totalLaw_easy = Law_easy.objects.all()
    randomLaw_easy = random.sample(list(totalLaw_easy), id)
    serializer = QuizSerializer(randomLaw_easy, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomLaw_normal(request, id):
    totalLaw_normal = Law_normal.objects.all()
    randomLaw_normal = random.sample(list(totalLaw_normal), id)
    serializer = QuizSerializer(randomLaw_normal, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomLaw_hard(request, id):
    totalLaw_hard = Law_hard.objects.all()
    randomLaw_hard = random.sample(list(totalLaw_hard), id)
    serializer = QuizSerializer(randomLaw_hard, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomTransit_easy(request, id):
    totalTransit_easy = Transit_easy.objects.all()
    randomTransit_easy = random.sample(list(totalTransit_easy), id)
    serializer = QuizSerializer(randomTransit_easy, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomTransit_normal(request, id):
    totalTransit_normal = Transit_normal.objects.all()
    randomTransit_normal = random.sample(list(totalTransit_normal), id)
    serializer = QuizSerializer(randomTransit_normal, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomTransit_hard(request, id):
    totalTransit_hard = Transit_hard.objects.all()
    randomTransit_hard = random.sample(list(totalTransit_hard), id)
    serializer = QuizSerializer(randomTransit_hard, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomSafety_easy(request, id):
    totalSafety_easy = Safety_easy.objects.all()
    randomSafety_easy = random.sample(list(totalSafety_easy), id)
    serializer = QuizSerializer(randomSafety_easy, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomSafety_normal(request, id):
    totalSafety_normal = Safety_normal.objects.all()
    randomSafety_normal = random.sample(list(totalSafety_normal), id)
    serializer = QuizSerializer(randomSafety_normal, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomSafety_hard(request, id):
    totalSafety_hard = Safety_hard.objects.all()
    randomSafety_hard = random.sample(list(totalSafety_hard), id)
    serializer = QuizSerializer(randomSafety_hard, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomService_easy(request, id):
    totalService_easy = Service_easy.objects.all()
    randomService_easy = random.sample(list(totalService_easy), id)
    serializer = QuizSerializer(randomService_easy, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomService_normal(request, id):
    totalService_normal = Service_normal.objects.all()
    randomService_normal = random.sample(list(totalService_normal), id)
    serializer = QuizSerializer(randomService_normal, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomService_hard(request, id):
    totalService_hard = Service_hard.objects.all()
    randomService_hard = random.sample(list(totalService_hard), id)
    serializer = QuizSerializer(randomService_hard, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomPractice(request, id):
    totalPractice = Practice.objects.all()
    randomPractice = random.sample(list(totalPractice), id)
    serializer = QuizSerializer(randomPractice, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomChallenge(request, id):
    totalChallenge = Challenge.objects.all()
    randomChallenge = random.sample(list(totalChallenge), id)
    serializer = QuizSerializer(randomChallenge, many=True)
    return Response(serializer.data)