# map the view in views.py to a url in urls.py
from django.urls import path

from . import views

# this contains the actual url patterns for polls app
urlpatterns = [
    path("" , views.index, name="index"),
]