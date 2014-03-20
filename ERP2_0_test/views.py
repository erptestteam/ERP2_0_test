# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db import transaction
from django.db import connection
from django.conf import settings
from django.utils import simplejson

import MySQLdb
from django.db import connection
from django.db import transaction
from django.utils import simplejson
import json
import re
import time
import datetime
import logging

from mysqldb_inspect import models as dbmodels

def index(request):
    now = datetime.datetime.now()
    now2 = datetime.datetime.utcnow()
    return HttpResponse('hello django.<br/>%s<br/>%s' % (now, now2))

def testdb(request):
    cursor = connection.cursor()
    cursor.execute('select id,d_time from ent_item where id = 1585')
    res = cursor.fetchall()
    print res
    return HttpResponse(simplejson.dumps(res, ensure_ascii=False))

def material_list(request):
    materialList = dbmodels.EntMaterial.objects.all().order_by('-id', 'name')
    # materialList = dbmodels.EntMaterial.objects.filter(name__contains='2m.')
    # materialList = dbmodels.EntMaterial.objects.filter(name__regex='.*2.*', id__lte=150).exclude(id=143).order_by('-id'，‘)
    jsonList = []
    for ma in materialList:
        # jsonList.append({'id':ma.id, 'name': ma.name})
        jsonList.append(ma.fullOBJ())
        '''
        new_obj = {}
        for (k, v) in ma.__dict__.items():
            if k != '_state':
                new_obj.setdefault(k, v)
        jsonList.append(new_obj)
        '''
    return HttpResponse(simplejson.dumps(jsonList, ensure_ascii=False))

def material_get(request):
    material = dbmodels.EntMaterial.objects.get(id=142)
    return HttpResponse(simplejson.dumps(material.fullOBJ(), ensure_ascii=False))

def material_add(request):
    nm = dbmodels.EntMaterial()
    nm.name = 'tes4'
    nm.save()
    print nm.id
    return HttpResponse('add material %s successful' % (nm.id))

def material_del(request, id):
    nm = dbmodels.EntMaterial()
    nm.id = id
    print nm.delete()
    return HttpResponse('del material %s successful' % (nm.id))

def entItem_del(request, del_id):
    print del_id
    obj_to_del = dbmodels.EntItem.objects.get(id=del_id)
    # print obj_to_del.delete()
    print obj_to_del.fullOBJ()
    obj_to_del.delete()
    return HttpResponse('del entItem %s successful' % (obj_to_del.id))
