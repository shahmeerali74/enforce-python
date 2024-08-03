from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import requests

def index(request):
    return render(request, 'index.html')