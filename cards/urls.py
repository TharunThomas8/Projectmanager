from django.urls import path
from . views import add_card,view_card,add_chat,CalendarView

urlpatterns = [
    path('add_card/',add_card,name='add_card'),
    path('add_chat/<int:cid>/',add_chat,name='add_chat'),
    path('view_card/<int:cid>/',view_card,name='view_card'),
    path('calendar/',CalendarView.as_view(),name='calendar')

]