from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.reg, name='reg'),
    path('succes/', views.reg_succes, name='succes')
]