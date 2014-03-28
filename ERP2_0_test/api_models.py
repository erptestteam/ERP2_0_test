# coding=utf-8
import datetime
import serializers
from django.utils.timezone import utc
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from django.utils import simplejson
from django.core.serializers import json
from django.conf.urls import url
from mysqldb_inspect import models as dbModels

class EntEquimentResource(ModelResource):
    class Meta:
        queryset = dbModels.EntEquipment.objects.all()
        resource_name = 'EntEquipment'
        allFields = dbModels.EntEquipment._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntEquipment.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntEquipment.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntItem.objects.all()
        resource_name = 'EntItem'
        allFields = dbModels.EntItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntItem.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntItem.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntMachineResource(ModelResource):
    class Meta:
        queryset = dbModels.EntMachine.objects.all()
        resource_name = 'EntMachine'
        allFields = dbModels.EntMachine._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntMachine.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntMachine.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntMaterialResource(ModelResource):
    class Meta:
        queryset = dbModels.EntMaterial.objects.all()
        resource_name = 'EntMaterial'
        allFields = dbModels.EntMaterial._meta.get_all_field_names()
        # excludes = ['id','']
        # fields = ['name', 'material_type']
        # include_resource_uri = False
        # allowed_methods = ['get', 'post']
        # limit = 100
        # ordering = ['id']
        # always_return_data = True
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        # obj_to_del = dbModels.EntMaterial.objects.get(id=int(kwargs['pk']))
        # obj_to_del = dbModels.EntMaterial.objects.get(**kwargs)
        # obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        # obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        print 'delete:', kwargs
        obj_to_del_List = dbModels.EntMaterial.objects.filter(**kwargs)
        for obj_to_del in obj_to_del_List:
            obj_to_del.d_time = datetime.datetime.now()
            # obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        print 'dellist:'
        print str(kwargs['request'])
        obj_to_delList = dbModels.EntMaterial.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntOrderResource(ModelResource):
    class Meta:
        queryset = dbModels.EntOrder.objects.all()
        resource_name = 'EntOrder'
        allFields = dbModels.EntOrder._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntOrder.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntOrder.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntRelItemItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntRelItemItem.objects.all()
        resource_name = 'EntRelItemItem'
        allFields = dbModels.EntRelItemItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntRelItemItem.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntRelItemItem.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntRelMathineItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntRelMachineItem.objects.all()
        resource_name = 'EntRelMachineItem'
        allFields = dbModels.EntRelMachineItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntRelMachineItem.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntRelMachineItem.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntRelStorageItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntRelStorageItem.objects.all()
        resource_name = 'EntRelStorageItem'
        allFields = dbModels.EntRelStorageItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntRelStorageItem.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntRelStorageItem.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntRelTechnologyItemEquipmentResource(ModelResource):
    class Meta:
        queryset = dbModels.EntRelTechnologyItemEquipment.objects.all()
        resource_name = 'EntRelTechnologyItemEquipment'
        allFields = dbModels.EntRelTechnologyItemEquipment._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntRelTechnologyItemEquipment.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntRelTechnologyItemEquipment.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntSotrageResource(ModelResource):
    class Meta:
        queryset = dbModels.EntStorage.objects.all()
        resource_name = 'EntStorage'
        allFields = dbModels.EntStorage._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntStorage.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntStorage.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class EntTechnologyResource(ModelResource):
    class Meta:
        queryset = dbModels.EntTechnology.objects.all()
        resource_name = 'EntTechnology'
        allFields = dbModels.EntTechnology._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntTechnology.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.EntTechnology.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()

class TmpItemFullRelResource(ModelResource):
    class Meta:
        queryset = dbModels.TmpItemFullRel.objects.all()
        resource_name = 'TmpItemFullRel'
        allFields = dbModels.TmpItemFullRel._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.TmpItemFullRel.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now()
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

    @classmethod    
    def obj_delete_list(self, bundle, **kwargs):
        obj_to_delList = dbModels.TmpItemFullRel.objects.filter(d_time__isnull=True)
        for obj_to_del in obj_to_delList:
            obj_to_del.d_time = datetime.datetime.now()
            obj_to_del.save()
