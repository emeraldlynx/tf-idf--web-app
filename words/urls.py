from django.urls import path

from .views import FileView

urlpatterns = [
    path('tf-idf/', FileView.as_view(), name='tf-idf'),
]
