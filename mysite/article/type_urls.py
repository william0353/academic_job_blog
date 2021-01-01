from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.type_list, name= 'type_list'),
    path('deep-search', views.deep_search, name= 'deep_search'),
    path('vacancies/', views.vacancies_view, name= 'vacancies' ),
    path('country/', views.country_view, name= 'country' ),
    path('dis/', views.dis_view, name= 'dis' ),
    path('rig/', views.rig_view, name= 'rig' ),
    path('ist/', views.ist_view, name= 'ist' ),
    path('result/', views.search_context, name= 'search_context' ),


]
