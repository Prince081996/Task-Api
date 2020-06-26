from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from rest_framework import status
import requests
from datetime import datetime
# Create your views here.

@api_view(['GET'])
def task(request):
    
    try:
        param_datetime = datetime.strptime(request.GET.get('DATETIME'), "%m/%d/%y %H:%M:%S")

    except:
         return HttpResponse('Datetime should be in format : 09/19/18 13:55:00')
    if param_datetime == datetime.now():
        try:
            api_request = requests.get(request.GET.get('URL'))
            return HttpResponse('Yes, it worked') if api_request.status_code == 200 else HttpResponse('The entered url failed with status code %s' %request.status_code)
        except:
            return HttpResponse('Entered URL is not reachable')
    else:
        return HttpResponse('Datetime does mot match with current datetime')


@api_view(['GET'])
def get(request):
    
    return JsonResponse({'status':'ok'})
