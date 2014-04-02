# coding=utf-8
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL
from tastypie.resources import ModelResource
from ERP2_0_test import mySerializers
from mysqldbmodels import models as dbModels


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