# coding=utf-8
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from ERP2_0_test import serializers
from ERP2_0_test.myModelResources import MyModelTrashResource
from mysqldbmodels import models as dbModels


class EntEquimentResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntEquipment.objects.all().order_by('-i_time', 'id')
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
    

class EntItemResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntItem.objects.all().order_by('-i_time', 'id')
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
    

class EntMachineResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntMachine.objects.all().order_by('-i_time', 'id')
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
    

class EntMaterialResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntMaterial.objects.all().order_by('-i_time', 'id')
        resource_name = 'EntMaterial'
        allFields = dbModels.EntMaterial._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()


class EntOrderResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntOrder.objects.all().order_by('-i_time', 'id')
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
    

class EntRelItemItemResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntRelItemItem.objects.all().order_by('-i_time', 'id')
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
    

class EntRelMathineItemResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntRelMachineItem.objects.all().order_by('-i_time', 'id')
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
    

class EntRelStorageItemResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntRelStorageItem.objects.all().order_by('-i_time', 'id')
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
    

class EntRelTechnologyItemEquipmentResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntRelTechnologyItemEquipment.objects.all().order_by('-i_time', 'id')
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
    

class EntSotrageResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntStorage.objects.all().order_by('-i_time', 'id')
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
    

class EntTechnologyResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.EntTechnology.objects.all().order_by('-i_time', 'id')
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
    

class TmpItemFullRelResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.TmpItemFullRel.objects.all().order_by('-i_time', 'id')
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
    

class TmpOrderResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.TmpOrder.objects.all().order_by('-i_time', 'id')
        resource_name = 'TmpOrder'
        allFields = dbModels.TmpOrder._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
        

class TmpOrderAnalysisResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.TmpOrderAnalysis.objects.all().order_by('-i_time', 'id')
        resource_name = 'TmpOrderAnalysis'
        allFields = dbModels.TmpOrderAnalysis._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
        

class TmpOrderFilterRelResource(MyModelTrashResource):
    class Meta:
        queryset = dbModels.TmpOrderFilter.objects.all().order_by('-i_time', 'id')
        resource_name = 'TmpOrderFilter'
        allFields = dbModels.TmpOrderFilter._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = serializers.TimeFormatSerializer()
        
