#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from djsonp import JSONPResponse,get_callback
import json
import jpush


def push(title,alert,builder_id=None,extras=None):
    app_key = '93daa86b9d7509857df57ada'
    master_secret = '31e92b183a024f9df79c3d91'
    _jpush = jpush.JPush(app_key, master_secret)
    push = _jpush.create_push()
    _jpush.set_logging('DEBUG')
    push.audience = jpush.all_
    _android = jpush.android(alert=alert, title=title, builder_id=builder_id,
                             extras=extras)
    push.notification = jpush.notification(android=_android)
    push.platform = jpush.all_
    try:
        response = push.send()
    except jpush.Unauthorized:
        raise jpush.Unauthorized('Unauthorized')
    except jpush.JPushFailure:
        raise jpush.JPushFailure('Jpush failure')
    except:
        print ('push error')


def index(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data), content_type="application/json")



def getDayHistory(request):


    return JSONPResponse(data={'foo': 'bar',}, callback= request.GET['callback'])


# Create your views here.
