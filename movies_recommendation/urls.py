from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^button/$', views.movies_recommendation, name='page1'),
]