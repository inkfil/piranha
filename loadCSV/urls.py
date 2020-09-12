from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexCSV, name='loadCSV_index'),
    path('uploadCSV/', views.uploadCSV, name='loadCSV_upload' )
]