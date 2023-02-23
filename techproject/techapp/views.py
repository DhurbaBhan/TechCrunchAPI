from django.shortcuts import render,HttpResponse
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json
# Create your views here.
@api_view(['GET', 'POST'])
def tech(request):
    if request.method == 'GET':
        prod=Post.objects.all()
        # result_list = list(prod)
        # return JsonResponse(json.dumps(result_list),safe=False)
        serial=PostSerializer(prod,many=True)
        return JsonResponse(serial.data,safe=False)
    
