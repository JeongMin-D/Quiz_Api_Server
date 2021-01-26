from django.urls import path, include
from .views import helloAPI, randomOX_hard, randomMul_hard, randomTest_hard
from .views import randomMul_easy, randomOX_easy, randomTest_easy
from .views import randomMul_normal, randomOX_normal, randomTest_normal

urlpatterns = [
    path('hello/', helloAPI),
    path('Mul_easy/<int:id>/', randomMul_easy),
    path('Mul_normal/<int:id>/', randomMul_normal),
    path('Mul_hard/<int:id>/', randomMul_hard),
    path('OX_easy/<int:id>/', randomOX_easy),
    path('OX_normal/<int:id>/', randomOX_normal),
    path('OX_hard/<int:id>/', randomOX_hard),
    path('Test_easy/<int:id>/', randomTest_easy),
    path('Test_normal/<int:id>/', randomTest_normal),
    path('Test_hard/<int:id>/', randomTest_hard)
]