from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Multiple, OX, Test
from .serializers import QuizSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')

@api_view(['GET'])
def randomMul_easy(request, id):
    totalMuls_easy = Multiple.objects.all()
    randomMuls_easy = random.sample(list(totalMuls_easy), id)
    serializer = QuizSerializer(randomMuls_easy, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomMul_normal(request, id):
    totalMuls_normal = Multiple.objects.all()
    randomMuls_normal = random.sample(list(totalMuls_normal), id)
    serializer = QuizSerializer(randomMuls_normal, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomMul_hard(request, id):
    totalMuls_hard = Multiple.objects.all()
    randomMuls_hard = random.sample(list(totalMuls_hard), id)
    serializer = QuizSerializer(randomMuls_hard, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomOX_easy(request, id):
    totalOXs_easy = OX.objects.all()
    randomOXs_easy = random.sample(list(totalOXs_easy), id)
    serializer = QuizSerializer(randomOXs_easy, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomOX_normal(request, id):
    totalOXs_normal = OX.objects.all()
    randomOXs_normal = random.sample(list(totalOXs_normal), id)
    serializer = QuizSerializer(randomOXs_normal, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomOX_hard(request, id):
    totalOXs_hard = OX.objects.all()
    randomOXs_hard = random.sample(list(totalOXs_hard), id)
    serializer = QuizSerializer(randomOXs_hard, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomTest_easy(request, id):
    totalTests_easy = Test.objects.all()
    randomTests_easy = random.sample(list(totalTests_easy), id)
    serializer = QuizSerializer(randomTests_easy, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomTest_normal(request, id):
    totalTests_normal = Test.objects.all()
    randomTests_normal = random.sample(list(totalTests_normal), id)
    serializer = QuizSerializer(randomTests_normal, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomTest_hard(request, id):
    totalTests_hard = Test.objects.all()
    randomTests_hard = random.sample(list(totalTests_hard), id)
    serializer = QuizSerializer(randomTests_hard, many=True)
    return Response(serializer.data)