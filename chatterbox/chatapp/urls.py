from django.urls import path
from . import views

urlpatterns = [
    path('chatapp/', views.chatter, name='chatapp'),
    path('chatapp/details/<int:id>', views.details, name='details'),
]
