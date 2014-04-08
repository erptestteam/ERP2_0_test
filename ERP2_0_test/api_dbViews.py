# coding=utf-8
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from tastypie.resources import ModelResource
from ERP2_0_test import mySerializers
from mysqldbmodels import models as dbModels


class VFeedingTrackingResource(ModelResource):
    class Meta:
        queryset = dbModels.VFeedingTracking.objects.all()
        resource_name = 'VFeedingTracking'
        allFields = dbModels.VFeedingTracking._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class VItemFullInfoResource(ModelResource):
    class Meta:
        queryset = dbModels.VItemFullInfo.objects.all()
        resource_name = 'VItemFullInfo'
        allFields = dbModels.VItemFullInfo._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class VOrderResource(ModelResource):
    class Meta:
        queryset = dbModels.VOrder.objects.all()
        resource_name = 'VOrder'
        allFields = dbModels.VOrder._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class VOrderAnalysisResource(ModelResource):
    class Meta:
        queryset = dbModels.VOrderAnalysis.objects.all()
        resource_name = 'VOrderAnalysis'
        allFields = dbModels.VOrderAnalysis._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class VOrderAnalysis2Resource(ModelResource):
    class Meta:
        queryset = dbModels.VOrderAnalysis2.objects.all()
        resource_name = 'VOrderAnalysis2'
        allFields = dbModels.VOrderAnalysis2._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class VOrderAnalysisGroupByNumberResource(ModelResource):
    class Meta:
        queryset = dbModels.VOrderAnalysisGroupByNumber.objects.all()
        resource_name = 'VOrderAnalysisGroupByNumber'
        allFields = dbModels.VOrderAnalysisGroupByNumber._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class VOrderFilterExtractResource(ModelResource):
    class Meta:
        queryset = dbModels.VOrderFilterExtract.objects.all()
        resource_name = 'VOrderFilterExtract'
        allFields = dbModels.VOrderFilterExtract._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    

class VOrderFindNewItemOrderResource(ModelResource):
    class Meta:
        queryset = dbModels.VOrderFindNewItemOrder.objects.all()
        resource_name = 'VOrderFindNewItemOrder'
        allFields = dbModels.VOrderFindNewItemOrder._meta.get_all_field_names()
        authorization = Authorization()
        ordering = allFields
        limit = 100
        max_limit = 0
        filtering = {}
        for field in allFields:
            filtering.setdefault(field, ALL)
        serializer = mySerializers.TimeFormatSerializer()
    
