from django.urls import path
from .views import ConverterAPIView

urlpatterns = [
    path('converter/', ConverterAPIView.as_view(), name='converter'),
] 