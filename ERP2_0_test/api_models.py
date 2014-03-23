# coding=utf-8
import datetime
from django.utils.timezone import utc
from tastypie.resources import ModelResource, Resource
from tastypie.resources import fields, Bundle
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from django.utils import simplejson
from django.core.serializers import json
import serializers

from mysqldb_inspect import models as dbModels 

class EntItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntItem.objects.all()
        resource_name = 'EntItem'
        authorization = Authorization()
        allFields = dbModels.EntItem._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntItem.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

class EntMachineResource(ModelResource):
    class Meta:
        queryset = dbModels.EntMachine.objects.all()
        resource_name = 'EntMachine'
        authorization = Authorization()
        allFields = dbModels.EntMachine._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntMachine.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

class EntMaterialResource(ModelResource):
    class Meta:
        queryset = dbModels.EntMaterial.objects.all()
        resource_name = 'EntMaterial'
        # excludes = ['id','']
        # fields = ['name', 'material_type']
        # include_resource_uri = False
        # allowed_methods = ['get']
        # Flimit = 100
        # ordering = ['id']
        authorization = Authorization()
        allFields = dbModels.EntMaterial._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntMaterial.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

class EntRelItemItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntRelItemItem.objects.all()
        resource_name = 'EntRelItemItem'
        authorization = Authorization()
        allFields = dbModels.EntRelItemItem._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntRelItemItem.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

class EntRelMathineItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntRelMathineItem.objects.all()
        resource_name = 'EntRelMathineItem'
        authorization = Authorization()
        allFields = dbModels.EntRelMathineItem._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntRelMathineItem.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

class EntRelStorageItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntRelStorageItem.objects.all()
        resource_name = 'EntRelStorageItem'
        authorization = Authorization()
        allFields = dbModels.EntRelStorageItem._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntRelStorageItem.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

class EntRelTechnologyItemEquipmentResource(ModelResource):
    class Meta:
        queryset = dbModels.EntRelTechnologyItemEquipment.objects.all()
        resource_name = 'EntRelTechnologyItemEquipment'
        authorization = Authorization()
        allFields = dbModels.EntRelTechnologyItemEquipment._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntRelTechnologyItemEquipment.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

class EntSotrageResource(ModelResource):
    class Meta:
        queryset = dbModels.EntStorage.objects.all()
        resource_name = 'EntStorage'
        authorization = Authorization()
        allFields = dbModels.EntStorage._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntStorage.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()

class EntTechnologyResource(ModelResource):
    class Meta:
        queryset = dbModels.EntTechnology.objects.all()
        resource_name = 'EntTechnology'
        authorization = Authorization()
        allFields = dbModels.EntTechnology._meta.get_all_field_names()
        ordering = allFields
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntTechnology.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()
