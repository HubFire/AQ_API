#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from djsonp import JSONPResponse,get_callback
import json

def index(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data), content_type="application/json")



def getDayHistory(request):


    return JSONPResponse(data={'foo': 'bar',}, callback= request.GET['callback'])


# Create your views here.
