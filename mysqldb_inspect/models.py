# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from django.db import models
from function import ERPFunction

class Alljo(models.Model):
    name = models.CharField(primary_key=True, max_length=255, blank=True)
    material_type = models.CharField(primary_key=True, max_length=33, blank=True)
    length = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'alljo'
#        unique_together = ("name")
#        unique_together = ("material_type", "name")

class EntItem(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, blank=True)
    meterial = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_item'

class EntMachine(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_machine'

class EntMaterial(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, blank=True)
    material_type = models.CharField(max_length=33, blank=True)
    length = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    radius = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = u'ent_material'

class EntRelItemItem(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    p_item_number = models.CharField(max_length=255, blank=True)
    c_item_number = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_rel_item_item'

class EntRelMathineItem(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    mathine_id = models.IntegerField(null=True, blank=True)
    item_number = models.CharField(max_length=255, blank=True)
    count = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_rel_mathine_item'

class EntRelStorageItem(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    storage_id = models.IntegerField(null=True, blank=True)
    item_number = models.CharField(max_length=255, blank=True)
    count = models.IntegerField(null=True, blank=True)
    safe_stock = models.IntegerField(null=True, blank=True)
    lock_count = models.IntegerField(null=True, blank=True)
    audit_time = models.DateTimeField(null=True, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_rel_storage_item'

class EntRelTechnologyItemEquipment(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    item_number = models.CharField(max_length=255, blank=True)
    technology_id = models.IntegerField(null=True, blank=True)
    dimensions = models.CharField(max_length=255, blank=True)
    mathine_id = models.IntegerField(null=True, blank=True)
    mathine_param = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField()
    u_time = models.DateTimeField()
    d_time = models.DateTimeField()
    class Meta:
        db_table = u'ent_rel_technology_item_equipment'

class EntStorage(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_storage'

class EntTechnology(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    descr = models.CharField(max_length=255, blank=True)
    remark = models.IntegerField(null=True, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_technology'

