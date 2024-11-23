from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def career(request):
    return render(request, "firstApp/all_files.html" )