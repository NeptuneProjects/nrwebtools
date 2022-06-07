from django.urls import path
from .views import Block29View
from . import views

urlpatterns = [
    path('', Block29View.as_view(), name='/block29app/'),
]
