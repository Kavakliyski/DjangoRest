# from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({'message:': 'Django Response'})