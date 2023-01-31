# from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):

    print(request.GET)  # urls query params
    print(request.POST)
    
    # take the request and turn it into a py dict
    body = request.body
    data = {}

    try:
        data = json.loads(body)
    except:
        pass

    print(data)
    # print(data.keys())

    # data['headers'] = request.headers
    # data['conent_type'] = request.conent_type
    print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)

    return JsonResponse(
        # {'message:': 'Django Response'}
        data
    )
