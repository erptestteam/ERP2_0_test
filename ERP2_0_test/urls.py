from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from tastypie.api import Api
import api
# from ERP2_0_test.api import EntMaterialResource, EntItemResource

v1_api = Api(api_name='v1')
v1_api.register(api.EntItemResource())
v1_api.register(api.EntMachineResource())
v1_api.register(api.EntMaterialResource())
v1_api.register(api.EntRelItemItemResource())
v1_api.register(api.EntRelStorageItemResource())
v1_api.register(api.EntRelTechnologyItemEquipmentResource())
v1_api.register(api.EntSotrageResource())
v1_api.register(api.EntTechnologyResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    url(r'^$', views.index),
    # url(r'^testdb/$', views.testdb),
    # url(r'^material/list/$', views.material_list),
    # url(r'^material/get/$', views.material_get),
    # url(r'^material/add/$', views.material_add),
    # url(r'^material/(.+)/del/$', views.material_del),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

