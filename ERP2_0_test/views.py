# coding=utf-8
from django.http import HttpResponse
from django.db import connection
from django.utils import simplejson
from django.core.serializers import json
import datetime
from mysqldbmodels import models as dbmodels


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
    nm.name = 'tes66'
    print nm.id
    nm.save()
    print nm.id
    return HttpResponse('add material %s successful' % (nm.id))


def material_del(request, mid):
    nm = dbmodels.EntMaterial()
    nm.id = mid
    print nm.delete()
    return HttpResponse('del material %s successful' % (nm.id))


def entItem_del(request, del_id):
    print del_id
    obj_to_del = dbmodels.EntItem.objects.get(id=del_id)
    # print obj_to_del.delete()
    print obj_to_del.fullOBJ()
    obj_to_del.delete()
    return HttpResponse('del entItem %s successful' % (obj_to_del.id))


def userDefinedSQL(request, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
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


def testAdvancedModelsFunction(request):
    responseSTR = ''
    material_list = dbmodels.EntMaterial.objects.filter(d_time__isnull=True).exclude()
    # material_list = dbmodels.EntMaterial.objects.exclude(d_time__isnull=True)
    for obj in material_list:
        responseSTR = responseSTR + str(obj.fullOBJ()) + '<br/>'
    now = datetime.datetime.now()
    utcnow = datetime.datetime.utcnow()
    return HttpResponse('testAdvancedModelsFunction.<br/>local:%s<br/>utc:%s<br>%s' % (now, utcnow,
                         simplejson.encoder(responseSTR)))

