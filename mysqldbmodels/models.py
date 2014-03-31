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

class EntEquipment(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_equipment'

class EntFeeding(models.Model):
    id = models.IntegerField(primary_key=True)
    item_number = models.CharField(max_length=255, blank=True)
    feeding_count = models.IntegerField(null=True, blank=True)
    feeding_date = models.DateTimeField(null=True, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_feeding'

class EntFeedingStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    feeding_id = models.IntegerField(null=True, blank=True)
    step_name = models.CharField(max_length=255, blank=True)
    step_status = models.CharField(max_length=765, blank=True)
    step_rang = models.IntegerField(null=True, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_feeding_status'

class EntItem(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, unique=True, blank=True)
    material = models.CharField(max_length=255, blank=True)
    type = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    defective_rate = models.FloatField(null=True, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_item'

class EntMachine(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, blank=True)
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

class EntOrder(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, unique=True, blank=True)
    batch_number = models.CharField(max_length=255, unique=True, blank=True)
    type = models.CharField(max_length=255, blank=True)
    note_date = models.DateTimeField(null=True, blank=True)
    item_number = models.CharField(max_length=255, blank=True)
    order_lead_time = models.DateField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_order'

class EntRelItemDrawing(models.Model):
    id = models.IntegerField(primary_key=True)
    item_number = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    disable = models.IntegerField(null=True, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_rel_item_drawing'

class EntRelItemItem(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    p_item_number = models.CharField(max_length=255, blank=True)
    c_item_number = models.CharField(max_length=255, blank=True)
    count = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_rel_item_item'

class EntRelMachineItem(models.Model, ERPFunction):
    id = models.IntegerField(primary_key=True)
    machine_id = models.IntegerField(unique=True, null=True, blank=True)
    item_number = models.CharField(max_length=765, blank=True)
    count = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=765, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_rel_machine_item'

class EntRelStorageItem(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    storage_id = models.IntegerField(null=True, blank=True)
    item_number = models.CharField(max_length=255, blank=True)
    actual_count = models.IntegerField(null=True, blank=True)
    min_count = models.IntegerField(null=True, blank=True)
    lock_count = models.IntegerField(null=True, blank=True)
    future_count = models.IntegerField(null=True, blank=True)
    audit_time = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ent_rel_storage_item'

class EntRelTechnologyItemEquipment(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    item_number = models.CharField(max_length=255, blank=True)
    technology_id = models.IntegerField(null=True, blank=True)
    technology_info = models.CharField(max_length=255, blank=True)
    dimensions = models.CharField(max_length=255, blank=True)
    equipment_id = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    equipment_param = models.CharField(max_length=255, blank=True)
    remark = models.CharField(max_length=255, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
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

class TmpItemFullRel(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    t = models.CharField(max_length=255)
    p = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    n = models.IntegerField(null=True, blank=True)
    n1 = models.IntegerField(null=True, blank=True)
    l = models.IntegerField(null=True, blank=True)
    leaf = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tmp_item_full_rel'

class TmpOrder(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, blank=True)
    batch_number = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    note_date = models.DateTimeField(null=True, blank=True)
    item_number = models.CharField(max_length=255, blank=True)
    order_lead_time = models.DateField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    i_time = models.DateTimeField(null=True, blank=True)
    u_time = models.DateTimeField(null=True, blank=True)
    d_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'tmp_order'

class TmpOrderAnalysis(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    orderid = models.IntegerField(null=True, db_column='orderID', blank=True)  # Field name made lowercase.
    componentid = models.CharField(max_length=255, db_column='componentID', blank=True)  # Field name made lowercase.
    p = models.CharField(max_length=255, blank=True)
    c = models.CharField(max_length=255, blank=True)
    orderrequirement = models.IntegerField(null=True, db_column='orderRequirement', blank=True)  # Field name made lowercase.
    splitrequirement = models.IntegerField(null=True, db_column='splitRequirement', blank=True)  # Field name made lowercase.
    otherrequirement = models.IntegerField(null=True, db_column='otherRequirement', blank=True)  # Field name made lowercase.
    defectrequirement = models.IntegerField(null=True, db_column='defectRequirement', blank=True)  # Field name made lowercase.
    actualstorage = models.IntegerField(null=True, db_column='actualStorage', blank=True)  # Field name made lowercase.
    futurestorage = models.IntegerField(null=True, db_column='futureStorage', blank=True)  # Field name made lowercase.
    usedstorage = models.IntegerField(null=True, db_column='usedStorage', blank=True)  # Field name made lowercase.
    fromstorage = models.IntegerField(null=True, db_column='fromStorage', blank=True)  # Field name made lowercase.
    fromproduct = models.IntegerField(null=True, db_column='fromProduct', blank=True)  # Field name made lowercase.
    n_full_rel = models.IntegerField(null=True, blank=True)
    nl_full_rel = models.IntegerField(null=True, blank=True)
    l_full_rel = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tmp_order_analysis'

class TmpOrderFilter(models.Model, ERPFunction):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, unique=True, blank=True)
    batch_number = models.CharField(max_length=255, unique=True, blank=True)
    type = models.CharField(max_length=255, blank=True)
    note_date = models.DateTimeField(null=True, blank=True)
    item_number = models.CharField(max_length=255, blank=True)
    order_lead_time = models.DateField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tmp_order_filter'
