# coding=utf-8
from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from tastypie.api import Api
from ERP2_0_test import api_models
from ERP2_0_test import api_trash
from ERP2_0_test import api_dbViews
from ERP2_0_test import api_udViews
# from ERP2_0_test.api_model import EntMaterialResource, EntItemResource

v1_api = Api(api_name='v1')
v1_api.register(api_models.EntEquimentResource())
v1_api.register(api_models.EntFeedingResource())
v1_api.register(api_models.EntFeedingStatusResource())
v1_api.register(api_models.EntItemResource())
v1_api.register(api_models.EntMachineResource())
v1_api.register(api_models.EntMaterialResource())
v1_api.register(api_models.EntMenuResource())
v1_api.register(api_models.EntOrderResource())
v1_api.register(api_models.EntRelItemDrawingResource())
v1_api.register(api_models.EntRelItemItemResource())
v1_api.register(api_models.EntRelMachineItemResource())
v1_api.register(api_models.EntRelStorageItemResource())
v1_api.register(api_models.EntRelTechnologyItemEquipmentResource())
v1_api.register(api_models.EntSotrageResource())
v1_api.register(api_models.EntStorageChangesRecordResource())
v1_api.register(api_models.EntTechnologyResource())
v1_api.register(api_models.EntUserResource())
v1_api.register(api_models.ItemTechnologyResource())
v1_api.register(api_models.StorageGroupByResource())
v1_api.register(api_models.TemporaryOrderFilterResource())
v1_api.register(api_models.TmpItemFullRelResource())
v1_api.register(api_models.TmpOrderResource())
v1_api.register(api_models.TmpOrderAnalysisResource())
v1_api.register(api_models.TmpOrderAnalysis2Resource())
v1_api.register(api_models.TmpOrderFilterResource())
v1_api.register(api_udViews.MessageResource())
v1_api.register(api_dbViews.VFeedingTrackingResource())
v1_api.register(api_dbViews.VItemFullInfoResource())
v1_api.register(api_dbViews.VItemFullStorageResource())
v1_api.register(api_dbViews.VOrderResource())
v1_api.register(api_dbViews.VOrderAnalysisResource())
v1_api.register(api_dbViews.VOrderAnalysis2Resource())
v1_api.register(api_dbViews.VOrderAnalysisGroupByNumberResource())
v1_api.register(api_dbViews.VOrderFilterExtractResource())
v1_api.register(api_dbViews.VOrderFindNewItemOrderResource())
v1_api.register(api_dbViews.VStorageItemGroupByItemResource())

trash_v1_api = Api(api_name='v1')
trash_v1_api.register(api_trash.EntEquimentResource())
trash_v1_api.register(api_trash.EntFeedingResource())
trash_v1_api.register(api_trash.EntFeedingStatusResource())
trash_v1_api.register(api_trash.EntItemResource())
trash_v1_api.register(api_trash.EntMachineResource())
trash_v1_api.register(api_trash.EntMaterialResource())
trash_v1_api.register(api_trash.EntMenuResource())
trash_v1_api.register(api_trash.EntOrderResource())
trash_v1_api.register(api_trash.EntRelItemDrawingResource())
trash_v1_api.register(api_trash.EntRelItemItemResource())
trash_v1_api.register(api_trash.EntRelMachineItemResource())
trash_v1_api.register(api_trash.EntRelStorageItemResource())
trash_v1_api.register(api_trash.EntRelTechnologyItemEquipmentResource())
trash_v1_api.register(api_trash.EntSotrageResource())
trash_v1_api.register(api_trash.EntStorageChangesRecordResource())
trash_v1_api.register(api_trash.EntTechnologyResource())
trash_v1_api.register(api_trash.EntUserResource())
# trash_v1_api.register(api_trash.TemporaryOrderFilterResource())
# trash_v1_api.register(api_trash.TmpItemFullRelResource())
# trash_v1_api.register(api_trash.TmpOrderResource())
# trash_v1_api.register(api_trash.TmpOrderAnalysisResource())
# trash_v1_api.register(api_trash.TmpOrderAnalysis2Resource())
# trash_v1_api.register(api_trash.TmpOrderFilterResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    (r'^api/trash/', include(trash_v1_api.urls)),
    url(r'^$', views.index),
    url(r'^superAPI/(.+)/$', views.userDefinedSQL),
    url(r'testAdvancedModelsFunction/$', views.testAdvancedModelsFunction),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
