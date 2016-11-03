#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from djsonp import JSONPResponse,get_callback
import json
from api.models import *

def index(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data), content_type="application/json")



def getDayHistory(request):

    return JSONPResponse(data={'foo': 'bar',}, callback= request.GET['callback'])


def getStockList(request):
    if request.method=='GET':
        start=request.GET['start']
        limit=request.GET['limit']
        data=m_getStockList(int(start),int(limit))
        result={}
        result['data']=data
        return JSONPResponse(result, callback=request.GET['callback'])


