from django.urls import path

from app.views import FakerView

urlpatterns = [path("faker/", FakerView.as_view())]
