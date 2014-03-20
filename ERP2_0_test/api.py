import datetime
from django.utils.timezone import utc
from tastypie.resources import ModelResource, Resource
from tastypie.resources import fields, Bundle
from tastypie.authorization import Authorization
from tastypie.resources import ALL_WITH_RELATIONS, ALL

from mysqldb_inspect import models as dbModels 

class EntItemResource(ModelResource):
    class Meta:
        queryset = dbModels.EntItem.objects.all()
        resource_name = 'EntItem'
        authorization = Authorization()
    
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
        authorization = Authorization()
        # Flimit = 100
        '''
        filtering = {
           "name": ALL,
           'id': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        '''
    
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
    
    @classmethod
    def obj_delete(self, bundle, **kwargs):
        obj_to_del = dbModels.EntTechnology.objects.get(id=int(kwargs['pk']))
        obj_to_del.d_time = datetime.datetime.now().replace(tzinfo=utc)
        #obj_to_del.d_time = datetime.datetime.utcnow()  # WROGN!!!
        obj_to_del.save()
    
class RiakObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data

class MessageResource(Resource):
    # Just like a Django ``Form`` or ``Model``, we're defining all the
    # fields we're going to handle with the API here.
    uuid = fields.CharField(attribute='uuid')
    user_uuid = fields.CharField(attribute='user_uuid')
    message = fields.CharField(attribute='message')
    created = fields.IntegerField(attribute='created')

    class Meta:
        resource_name = 'riak'
        object_class = RiakObject
        authorization = Authorization()

    # Specific to this resource, just to get the needed Riak bits.
    def _client(self):
        return self.RiakClient()

    def _bucket(self):
        client = self._client()
        # Note that we're hard-coding the bucket to use. Fine for
        # example purposes, but you'll want to abstract this.
        return client.bucket('messages')

    # The following methods will need overriding regardless of your
    # data source.
    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.uuid
        else:
            kwargs['pk'] = bundle_or_obj.uuid

        return kwargs

    def get_object_list(self, request):
        query = self._client().add('messages')
        query.map("function(v) { var data = JSON.parse(v.values[0].data); return [[v.key, data]]; }")
        results = []

        for result in query.run():
            new_obj = RiakObject(initial=result[1])
            new_obj.uuid = result[0]
            results.append(new_obj)

        return results

    def obj_get_list(self, request=None, **kwargs):
        # Filtering disabled for brevity...
        return self.get_object_list(request)

    def obj_get(self, request=None, **kwargs):
        bucket = self._bucket()
        message = bucket.get(kwargs['pk'])
        return RiakObject(initial=message.get_data())

    def obj_create(self, bundle, request=None, **kwargs):
        bundle.obj = RiakObject(initial=kwargs)
        bundle = self.full_hydrate(bundle)
        bucket = self._bucket()
        new_message = bucket.new(bundle.obj.uuid, data=bundle.obj.to_dict())
        new_message.store()
        return bundle

    def obj_update(self, bundle, request=None, **kwargs):
        return self.obj_create(bundle, request, **kwargs)

    def obj_delete_list(self, request=None, **kwargs):
        bucket = self._bucket()

        for key in bucket.get_keys():
            obj = bucket.get(key)
            obj.delete()

    def obj_delete(self, request=None, **kwargs):
        bucket = self._bucket()
        obj = bucket.get(kwargs['pk'])
        obj.delete()

    def rollback(self, bundles):
        pass
