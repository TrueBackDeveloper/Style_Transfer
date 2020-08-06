from django.urls import path
from . import views

app_name = 'Style_Transfer_Application'

urlpatterns = [
    path('uploadimg/', views.upload_img, name='upload_img'),
    path('downloadimg/', views.download_img, name='download_img'),
]
