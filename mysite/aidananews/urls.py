from django.urls import path
from . import views
app_name = "aidananews"
urlpatterns = [
    path("", views.index, name="index"),
]