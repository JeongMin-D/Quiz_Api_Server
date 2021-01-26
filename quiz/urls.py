from django.urls import path, include
from .views import helloAPI, randomOX_hard ,randomMul_hard, randomTest_hard
from .views import randomMul_easy, randomOX_easy, randomTest_easy
from .views import randomMul_normal, randomOX_normal, randomTest_normal

urlpatterns = [
    path('hello/', helloAPI),
    path('Mul/<int:id>/', randomMul_easy),
    path('Mul/<int:id>/', randomMul_normal),
    path('Mul/<int:id>/', randomMul_hard),
    path('OX/<int:id>/', randomOX_easy),
    path('OX/<int:id>/', randomOX_normal),
    path('OX/<int:id>/', randomOX_hard),
    path('Test/<int:id>/', randomTest_easy),
    path('Test/<int:id>/', randomTest_normal),
    path('Test/<int:id>/', randomTest_hard)
]