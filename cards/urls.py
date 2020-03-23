from django.urls import path
from . views import add_card,view_card

urlpatterns = [
    path('add_card/',add_card,name='add_card'),
    path('view_card/<int:cid>/',view_card,name='view_card')
]