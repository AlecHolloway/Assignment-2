from django.urls import path

from .views import HomeView, BMIView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('BMI', BMIView.as_view(), name='BMI'),
]
