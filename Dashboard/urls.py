from django.urls import path
from . import views

urlpatterns = [
    path('latest/', views.getimage, name='image'),
    path('daterange',views.daterange(), name='owen')
]