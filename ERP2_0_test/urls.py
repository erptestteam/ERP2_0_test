# coding=utf-8
from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from tastypie.api import Api
from ERP2_0_test import api_models
from ERP2_0_test import api_trash
from ERP2_0_test import api_views
# from ERP2_0_test.api_model import EntMaterialResource, EntItemResource

v1_api = Api(api_name='v1')
v1_api.register(api_models.EntEquimentResource())
v1_api.register(api_models.EntItemResource())
v1_api.register(api_models.EntMachineResource())
v1_api.register(api_models.EntMaterialResource())
v1_api.register(api_models.EntOrderResource())
v1_api.register(api_models.EntRelItemItemResource())
v1_api.register(api_models.EntRelMathineItemResource())
v1_api.register(api_models.EntRelStorageItemResource())
v1_api.register(api_models.EntRelTechnologyItemEquipmentResource())
v1_api.register(api_models.EntSotrageResource())
v1_api.register(api_models.EntTechnologyResource())
v1_api.register(api_models.TmpItemFullRelResource())
# v1_api.register(api_models.testviewResource())
v1_api.register(api_views.MessageResource())

trash_api = Api(api_name='v1')
trash_api.register(api_trash.EntEquimentResource())
trash_api.register(api_trash.EntItemResource())
trash_api.register(api_trash.EntMachineResource())
trash_api.register(api_trash.EntMaterialResource())
trash_api.register(api_trash.EntOrderResource())
trash_api.register(api_trash.EntRelItemItemResource())
trash_api.register(api_trash.EntRelMathineItemResource())
trash_api.register(api_trash.EntRelStorageItemResource())
trash_api.register(api_trash.EntRelTechnologyItemEquipmentResource())
trash_api.register(api_trash.EntSotrageResource())
trash_api.register(api_trash.EntTechnologyResource())
trash_api.register(api_trash.TmpItemFullRelResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    (r'^api/trash/', include(trash_api.urls)),
    url(r'^$', views.index),
    url(r'^superAPI/(.+)/$', views.userDefinedSQL),
    # url(r'^deleteList/(.+)/set/(.+)/$', views.deleteList),
    # url(r'^testdb/$', views.testdb),
    # url(r'^material/list/$', views.material_list),
    # url(r'^material/get/$', views.material_get),
    # url(r'^material/add/$', views.material_add),
    # url(r'^material/(.+)/del/$', views.material_del),
    # url(r'^EntItem/(.+)/del/$', views.entItem_del),
    url(r'testAdvancedModelsFunction/$', views.testAdvancedModelsFunction),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
