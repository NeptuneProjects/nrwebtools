from django.urls import path
from . import views

urlpatterns = [
    path('', views.Block29View.as_view(), name='/block29app/'),
]
