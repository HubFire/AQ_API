from __future__ import unicode_literals

from django.db import models
import jpush
# Create your models here.


import pymongo
from pymongo import MongoClient

DB_IP = '192.168.1.192'
client = MongoClient(DB_IP,port=27017)


def m_getStockList(start=0,limit=10):
    basic_col =client.stock.stock_basic
    data = basic_col.find({},{'_id':0}).sort([('code',1)]).skip(start).limit(limit)
    return list(data)

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

def m_getIndexList():

    index_today_col =client.index.index_today
    data = index_today_col.find({},{'_id': 0}).sort([('code', 1)])
    return list(data)

def m_getHotStock():
    hotStock_col= client.recommend.hot_stock
    data = hotStock_col.find({},{'_id': 0})
    return list(data)