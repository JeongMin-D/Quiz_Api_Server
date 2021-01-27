from django.urls import path, include
from .views import helloAPI, OX_law, OX_safety, OX_service, OX_transit
from .views import Law_easy, Law_normal, Law_hard, Transit_easy, Transit_normal, Transit_hard
from .views import Safety_easy, Safety_normal, Safety_hard, Service_easy, Service_normal, Service_hard
from .views import Practice, Challenge

urlpatterns = [
    path('hello/', helloAPI),
    path('OX_law/<int:id>/', randomOX_law),
    path('OX_safety/<int:id>/', randomOX_safety),
    path('OX_service/<int:id>/', randomOX_service),
    path('OX_transit/<int:id>/', randomOX_transit),
    path('Law_easy/<int:id>/', randomLaw_easy),
    path('Law_normal/<int:id>/', randomLaw_normal),
    path('Law_hard/<int:id>/', randomLaw_hard),
    path('Transit_easy/<int:id>/', randomTransit_easy),
    path('Transit_normal/<int:id>/', randomTransit_normal),
    path('Transit_hard/<int:id>/', randomTransit_hard),
    path('Safety_easy/<int:id>/', randomSafety_easy),
    path('Safety_normal/<int:id>/', randomSafety_normal),
    path('Safety_hard/<int:id>/', randomSafety_hard),
    path('Service_easy/<int:id>/', randomService_easy),
    path('Service_normal/<int:id>/', randomService_normal),
    path('Service_hard/<int:id>/', randomService_hard),
    path('Practice/<int:id>/', randomPractice),
    path('Challenge/<int:id>/', randomChallenge),
]