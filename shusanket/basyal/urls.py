import imp

from .views import hello
from django.urls import path

urlpatterns = [
    path("get", hello),
    path("get/<int:pk>", hello)

]
