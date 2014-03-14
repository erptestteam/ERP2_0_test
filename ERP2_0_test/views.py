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

def testdb2(request):
    materialList = dbmodels.EntMaterial.objects.all()
    jsonList = []
    for ma in materialList:
        jsonList.append({'id':ma.id, 'name': ma.name})
    return HttpResponse(simplejson.dumps(jsonList, ensure_ascii=False))

