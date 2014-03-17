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
import logging

from mysqldb_inspect import models as dbmodels

def index(request):
    return HttpResponse('hello django.')

def testdb(request):
    cursor = connection.cursor()
    cursor.execute('select id,name,material_type from ent_material')
    res = cursor.fetchall()
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
    nm = dbmodels.EntMaterial.objects.get(id=142)
    rnm = {'id':nm.id, 'name': nm.name}
    return HttpResponse(simplejson.dumps(rnm, ensure_ascii=False))

def material_add(request):
    nm = dbmodels.EntMaterial
    nm.name = 'test'
    nm.save()
    print type(nm)
    
    return HttpResponse(0)
