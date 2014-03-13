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
import MySQLdb
from django.conf import settings

def index(request):
    return HttpResponse('heloo,e')
