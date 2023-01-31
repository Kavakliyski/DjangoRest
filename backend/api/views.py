# from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse, HttpResponse

from django.forms.models import model_to_dict
  
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """

    print(request.GET)  # urls query params
    print(request.POST)

    instance = Product.objects.all().order_by("?").first()
    data = {}

    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price

    if instance:
        # data = model_to_dict(model_data)
        data = ProductSerializer(instance).data

    return JsonResponse(data)
