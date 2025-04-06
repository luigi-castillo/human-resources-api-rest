from django.urls import include, path
from .views import UploadAPIView

urlpatterns = [
    path('api/upload/', UploadAPIView.as_view(), name='upload-file'),
]