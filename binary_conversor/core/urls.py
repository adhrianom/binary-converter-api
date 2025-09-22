from django.urls import path
from .views import converter

urlpatterns = [
    path('converter/', converter, name='converter'),
]