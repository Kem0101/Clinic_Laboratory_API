# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Laboratorytest(models.Model):
    test_id = models.AutoField(primary_key=True)
    testname = models.CharField(max_length=100)
    description = models.TextField()
    cpt_code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'LaboratoryTest'


class Medical(models.Model):
    medical_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=100)
    exequatur = models.CharField(unique=True, max_length=20, blank=True, null=True)
    id_card = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'Medical'


class Orderdetail(models.Model):
    test = models.OneToOneField(Laboratorytest, models.DO_NOTHING, primary_key=True)  # The composite primary key (test_id, order_id) found, that is not supported. The first column is selected.
    order = models.ForeignKey('Testorder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'OrderDetail'
        unique_together = (('test', 'order'),)


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    id_card = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'Patient'


class Testorder(models.Model):
    order_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    medical = models.ForeignKey(Medical, models.DO_NOTHING)
    date_time = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestOrder'


class Testresult(models.Model):
    result_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    test = models.ForeignKey(Laboratorytest, models.DO_NOTHING)
    medical = models.ForeignKey(Medical, models.DO_NOTHING)
    date_time = models.DateTimeField(blank=True, null=True)
    result_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit_measure = models.CharField(max_length=20, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestResult'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
