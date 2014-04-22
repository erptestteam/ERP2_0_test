# coding=utf-8
from django.http import HttpResponse
from django.db import connection
from django.db import transaction
from django.utils import simplejson
# from django.core.serializers import json
import json
import datetime
from mysqldbmodels import models as dbmodels
from django.conf import settings

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def index(request):
    return HttpResponse('hello django.<br/>%s<br/>local: %s<br/>utc:%s' % (
                        settings.DATABASES, datetime.datetime.now(), datetime.datetime.utcnow()))


@transaction.commit_on_success
def userDefinedSQL(request, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    res = ''
    try:
        res = cursor.fetchall()
    except:
        res = 'no output'
    return HttpResponse(simplejson.dumps(res))


model_talbe_map_list = [
                        {'model':dbmodels.EntEquipment, 'model_name':'EntEquipment', 'table_name':'ent_equipment'},
                        {'model':dbmodels.EntItem, 'model_name':'EntItem', 'table_name':'ent_item'},
                        {'model':dbmodels.EntMachine, 'model_name':'EntMachine', 'table_name':'ent_machine'},
                        {'model':dbmodels.EntMaterial, 'model_name':'EntMaterial', 'table_name':'ent_material'},
                        {'model':dbmodels.EntOrder, 'model_name':'EntOrder', 'table_name':'ent_order'},
                        {'model':dbmodels.EntRelItemItem, 'model_name':'EntRelItemItem', 'table_name':'ent_rel_item_item'},
                        {'model':dbmodels.EntRelMachineItem, 'model_name':'EntRelMachineItem', 'table_name':'ent_rel_machine_item'},
                        {'model':dbmodels.EntRelStorageItem, 'model_name':'EntRelStorageItem', 'table_name':'ent_rel_storage_item'},
                        {'model':dbmodels.EntRelTechnologyItemEquipment, 'model_name':'EntRelTechnologyItemEquipment', 'table_name':'ent_rel_technology_item_equipment'},
                        {'model':dbmodels.EntStorage, 'model_name':'EntStorage', 'table_name':'ent_storage'},
                        {'model':dbmodels.EntTechnology, 'model_name':'EntTechnology', 'table_name':'ent_technology'},
                        {'model':dbmodels.TmpItemFullRel, 'model_name':'TmpItemFullRel', 'table_name':'tmp_item_full_rel'},
                        ]


def deleteList(request, mo_na, to_del):
    to_del_obj_list = []
    to_del_list = to_del.split(';')
    for mtm in model_talbe_map_list:
        if mtm['model_name'] == mo_na:
            to_del_obj_list = mtm['model'].objects.filter(id__in=to_del_list)
    for tdo in to_del_obj_list:
        tdo.d_time = datetime.datetime.now()
        tdo.save()
    return HttpResponse(0)


from django.db.models import F
from django.db.models import Q
from datetime import timedelta

def testAdvancedModelsFunction(request):
    # material_list = dbmodels.EntMaterial.objects.filter(d_time__isnull=True).exclude()
    # material_list = dbmodels.EntMaterial.objects.exclude(d_time__isnull=True)
    # material_list = dbmodels.EntMaterial.objects.filter(length__gt=F('width'))
    # material_list = dbmodels.EntMaterial.objects.filter(d_time__lte=F('i_time') + timedelta(days=1))
    # material = dbmodels.EntMaterial.objects.get(id__exact=3)  # Explicit form
    # material = dbmodels.EntMaterial.objects.get(id=3)  # __exact is implied
    # material = dbmodels.EntMaterial.objects.get(pk=3)  # pk implies id__exact
    # material_list = dbmodels.EntMaterial.objects.filter(Q(id__lte=2) | Q(id__gte=20), Q(id__lte=22))
    material_list = dbmodels.EntMaterial.objects.filter(id__lte=2).values()
    material_list = dbmodels.EntMaterial.objects.filter(id__lte=10).values('id', 'name')
    # dbmodels.EntMaterial.objects.get(id__exact=1).delete()
    return HttpResponse('testAdvancedModelsFunction.<br/>local:%s<br/>utc:%s<br>%s' % (
                        datetime.datetime.now(), datetime.datetime.utcnow(), material_list))

