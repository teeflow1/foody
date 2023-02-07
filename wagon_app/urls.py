from django.urls import path

from wagon_app import views

urlpatterns = [
    path('', views.wagon_app, name ='wagon_app' )
]