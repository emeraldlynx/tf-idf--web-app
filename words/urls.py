from django.urls import path, re_path

from .views import TFIDFView, FileUploadView

urlpatterns = [
    re_path(r'^tf-idf/$', TFIDFView.as_view(), name='tf-idf'),
    re_path(r'^api/calculate-tf-idf/(?P<filename>[^/]+)$', FileUploadView.as_view(), name='calculate-tf-idf'),
]
