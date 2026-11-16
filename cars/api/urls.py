from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarsListCreateApiView.as_view()),
    path('detail/<int:id>/', views.CardetailListApiView.as_view())
]
