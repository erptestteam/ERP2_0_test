# coding=utf-8
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from ERP2_0_test import mySerializers
from ERP2_0_test import myModelResources
from mysqldbmodels import models as dbModels


class EntEquimentResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntEquipment.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntEquipment'
        allFields = dbModels.EntEquipment._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntItemResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntItem.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntItem'
        allFields = dbModels.EntItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntMachineResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntMachine.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntMachine'
        allFields = dbModels.EntMachine._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntMaterialResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntMaterial.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntMaterial'
        allFields = dbModels.EntMaterial._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()


class EntOrderResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntOrder.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntOrder'
        allFields = dbModels.EntOrder._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntRelItemDrawingResource(myModelResources.ENTModelResource):
    class Meta:
        queryset = dbModels.EntRelItemDrawing.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntRelItemDrawing'
        allFields = dbModels.EntRelItemDrawing._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()


class EntRelItemItemResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntRelItemItem.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntRelItemItem'
        allFields = dbModels.EntRelItemItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntRelMachineItemResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntRelMachineItem.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntRelMachineItem'
        allFields = dbModels.EntRelMachineItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntRelStorageItemResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntRelStorageItem.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntRelStorageItem'
        allFields = dbModels.EntRelStorageItem._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntRelTechnologyItemEquipmentResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntRelTechnologyItemEquipment.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntRelTechnologyItemEquipment'
        allFields = dbModels.EntRelTechnologyItemEquipment._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntSotrageResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntStorage.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntStorage'
        allFields = dbModels.EntStorage._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntTechnologyResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.EntTechnology.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntTechnology'
        allFields = dbModels.EntTechnology._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class TmpItemFullRelResource(myModelResources.TrashModelResource):
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
        serializer = mySerializers.TimeFormatSerializer()
        

class TmpOrderAnalysisResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.TmpOrderAnalysis.objects.all()
        resource_name = 'TmpOrderAnalysis'
        allFields = dbModels.TmpOrderAnalysis._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
        

class TmpOrderFilterRelResource(myModelResources.TrashModelResource):
    class Meta:
        queryset = dbModels.TmpOrderFilter.objects.all()
        resource_name = 'TmpOrderFilter'
        allFields = dbModels.TmpOrderFilter._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
        
