from django.urls import path
from . import views

app_name = 'homework'
urlpatterns = [
    path('', views.homework_list, name='homework_list'),
    path('homework_create_page/', views.homework_create_page, name='homework_create_page'),
    path('homework_create_page_success/', views.homework_create_page_success, name='homework_create_page_success'),
    path('search/', views.search, name='search'),
    path('search/<int:date_url>/', views.resalt, name='resalt'),
    path('tomorrow', views.tomorrow, name='tomorrow')
]