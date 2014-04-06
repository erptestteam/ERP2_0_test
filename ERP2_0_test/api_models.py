# coding=utf-8
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from ERP2_0_test import mySerializers
from ERP2_0_test import myModelResources
from mysqldbmodels import models as dbModels


class EntEquimentResource(myModelResources.ENTModelResource):
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
    

class EntFeedingResource(myModelResources.ENTModelResource):
    class Meta:
        queryset = dbModels.EntFeeding.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntFeeding'
        allFields = dbModels.EntFeeding._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntFeedingStatusResource(myModelResources.ENTModelResource):
    class Meta:
        queryset = dbModels.EntFeedingStatus.objects.all().order_by('step_rank', 'id')
        resource_name = 'EntFeedingStatus'
        allFields = dbModels.EntFeedingStatus._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntItemResource(myModelResources.ENTModelResource):
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
    

class EntMachineResource(myModelResources.ENTModelResource):
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
    

class EntMaterialResource(myModelResources.ENTModelResource):
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
    

class EntMenuResource(myModelResources.ENTModelResource):
    class Meta:
        queryset = dbModels.EntMenu.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntMenu'
        allFields = dbModels.EntMenu._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntOrderResource(myModelResources.ENTModelResource):
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
    

class EntRelItemItemResource(myModelResources.ENTModelResource):
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
    

class EntRelMachineItemResource(myModelResources.ENTModelResource):
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
    

class EntRelStorageItemResource(myModelResources.ENTModelResource):
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
    

class EntRelTechnologyItemEquipmentResource(myModelResources.ENTModelResource):
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
    

class EntSotrageResource(myModelResources.ENTModelResource):
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
    

class EntStorageChangesRecordResource(myModelResources.ENTModelResource):
    class Meta:
        queryset = dbModels.EntStorageChangesRecord.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntStorageChangesRecord'
        allFields = dbModels.EntStorageChangesRecord._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class EntTechnologyResource(myModelResources.ENTModelResource):
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
    

class EntUserResource(myModelResources.ENTModelResource):
    class Meta:
        queryset = dbModels.EntUser.objects.all().order_by('-u_time', 'id')
        resource_name = 'EntUser'
        allFields = dbModels.EntUser._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class TmpItemFullRelResource(myModelResources.TMPModelResource):
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
    

class TmpOrderResource(myModelResources.TMPModelResource):
    class Meta:
        queryset = dbModels.TmpOrder.objects.all()
        resource_name = 'TmpOrder'
        allFields = dbModels.TmpOrder._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class TmpOrderAnalysisResource(myModelResources.TMPModelResource):
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
    

class TmpOrderAnalysis2Resource(myModelResources.TMPModelResource):
    class Meta:
        queryset = dbModels.TmpOrderAnalysis2.objects.all()
        resource_name = 'TmpOrderAnalysis2'
        allFields = dbModels.TmpOrderAnalysis2._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class TmpOrderFilterResource(myModelResources.TMPModelResource):
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
    
