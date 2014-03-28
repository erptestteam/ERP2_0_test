# coding=utf-8
import django
import datetime
import serializers
from tastypie import http
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError
from tastypie.utils import is_valid_jsonp_callback_value, dict_strip_unicode_keys, trailing_slash
from tastypie.exceptions import NotFound, BadRequest, InvalidFilterError, HydrationError, InvalidSortError, ImmediateHttpResponse, Unauthorized

class MyModelResource(ModelResource):
    def obj_get_list(self, bundle, **kwargs):
        filters = {}

        if hasattr(bundle.request, 'GET'):
            # Grab a mutable copy.
            filters = bundle.request.GET.copy()
        # Update with the provided kwargs.
        filters.update(kwargs)
        filters.setdefault('d_time__isnull', 'True')
        applicable_filters = self.build_filters(filters=filters)

        try:
            objects = self.apply_filters(bundle.request, applicable_filters)
            return self.authorized_read_list(objects, bundle)
        except ValueError:
            raise BadRequest("Invalid resource lookup data provided (mismatched type).")
    
    def obj_delete(self, bundle, **kwargs):
        if not hasattr(bundle.obj, 'delete'):
            try:
                bundle.obj = self.obj_get(bundle=bundle, **kwargs)
            except ObjectDoesNotExist:
                raise NotFound("A model instance matching the provided arguments could not be found.")

        self.authorized_delete_detail(self.get_object_list(bundle.request), bundle)
        # bundle.obj.delete()
        bundle.obj.d_time = datetime.datetime.now()
        bundle.obj.save()

    def obj_delete_list(self, bundle, **kwargs):
        objects_to_delete = self.obj_get_list(bundle=bundle, **kwargs)
        objects_to_delete = objects_to_delete.ap
        deletable_objects = self.authorized_delete_list(objects_to_delete, bundle)
        
        if hasattr(deletable_objects, 'delete'):
            # deletable_objects.delete()
            print 'true'
            for deleteable_object in deletable_objects:
                # if deleteable_object.d_time == None:
                print deleteable_object.id
                # deleteable_object.d_time = datetime.datetime.now()
                # deleteable_object.save()
        else:
            print 'false'
            for authed_obj in deletable_objects:
                # authed_obj.delete()
                authed_obj.d_time = datetime.datetime.now()
                authed_obj.save()

class MyModelTrashResource(ModelResource):
    def obj_get_list(self, bundle, **kwargs):
        filters = {}

        if hasattr(bundle.request, 'GET'):
            # Grab a mutable copy.
            filters = bundle.request.GET.copy()
        # Update with the provided kwargs.
        filters.update(kwargs)
        filters.setdefault('d_time__isnull', 'False')
        applicable_filters = self.build_filters(filters=filters)

        try:
            objects = self.apply_filters(bundle.request, applicable_filters)
            return self.authorized_read_list(objects, bundle)
        except ValueError:
            raise BadRequest("Invalid resource lookup data provided (mismatched type).")