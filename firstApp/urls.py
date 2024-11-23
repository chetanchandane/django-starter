
from django.urls import path, include 
from . import views

urlpatterns = [ 

    #first app urls include here
    path("", views.career, name="career")
]
