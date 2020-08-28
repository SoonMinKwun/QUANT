from django.shortcuts import render
from django.http import HttpResponse


#create ... views

def post_list(request):
    return HttpResponse("되나")