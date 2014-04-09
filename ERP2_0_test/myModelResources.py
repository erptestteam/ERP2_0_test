# coding=utf-8
import datetime
from tastypie.resources import ModelResource
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError
from tastypie.utils import is_valid_jsonp_callback_value, dict_strip_unicode_keys, trailing_slash
from tastypie.exceptions import NotFound, BadRequest, InvalidFilterError, HydrationError, InvalidSortError, ImmediateHttpResponse, Unauthorized


class ENTModelResource(ModelResource):
    '''
    def apply_filters(self, request, applicable_filters):
        distinct = request.GET('distinct', False) == 'True'
        if distinct:
            return self.get_object_list(request).filter(**applicable_filters).distinct()
        else:
            return self.get_object_list(request).filter(**applicable_filters)
    '''
    def save(self, bundle, skip_errors=False):
        self.is_valid(bundle)

        if bundle.errors and not skip_errors:
            raise ImmediateHttpResponse(response=self.error_response(bundle.request, bundle.errors))

        # Check if they're authorized.
        time_now = datetime.datetime.now()
        if bundle.obj.pk:
            self.authorized_update_detail(self.get_object_list(bundle.request), bundle)
            setattr(bundle.obj, 'u_time', time_now)
        else:
            self.authorized_create_detail(self.get_object_list(bundle.request), bundle)
            setattr(bundle.obj, 'u_time', time_now)
            setattr(bundle.obj, 'i_time', time_now)

        # Save FKs just in case.
        self.save_related(bundle)

        # Save the main object.
        bundle.obj.save()
        bundle.objects_saved.add(self.create_identifier(bundle.obj))

        # Now pick up the M2M bits.
        m2m_bundle = self.hydrate_m2m(bundle)
        self.save_m2m(m2m_bundle)
        return bundle
    
    
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
            for deleteable_object in deletable_objects:
                # if deleteable_object.d_time == None:
                print deleteable_object.id
                # deleteable_object.d_time = datetime.datetime.now()
                # deleteable_object.save()
        else:
            for authed_obj in deletable_objects:
                # authed_obj.delete()
                authed_obj.d_time = datetime.datetime.now()
                authed_obj.save()
        

class TMPModelResource(ModelResource):
    '''
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
            for deleteable_object in deletable_objects:
                # if deleteable_object.d_time == None:
                print deleteable_object.id
                # deleteable_object.d_time = datetime.datetime.now()
                # deleteable_object.save()
        else:
            for authed_obj in deletable_objects:
                # authed_obj.delete()
                authed_obj.d_time = datetime.datetime.now()
                authed_obj.save()
    '''
    

class TrashModelResource(ModelResource):
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
