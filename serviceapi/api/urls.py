from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('tickets/', views.Home.as_view()),
    path('index/<int:pk>', views.index),
    path('react/api/orders', views.OrderCreateList.as_view()),
]
