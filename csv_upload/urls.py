from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='csv_upload.views.upload_file'),
    path('upload/success/', views.upload_file_success),
    path('get/<str:numdos>/', views.get_document, name='csv_upload.views.get_document'),
]
