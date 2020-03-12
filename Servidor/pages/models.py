# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mediciones(models.Model):
    id_planta = models.ForeignKey('Planta', models.DO_NOTHING, db_column='id_Planta')  # Field name made lowercase.
    fecha = models.DateTimeField()
    humedad = models.FloatField(blank=True, null=True)
    temperatura = models.FloatField(blank=True, null=True)
    polucion = models.FloatField(blank=True, null=True)
    nivelbajo = models.FloatField(blank=True, null=True)
    nivelalto = models.FloatField(blank=True, null=True)
    luz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mediciones'


class Planta(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.TextField()
    fecha_plantado = models.DateTimeField()
    proveedor = models.TextField()
    id_plantador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_plantador')
    id_tecnica = models.ForeignKey('Tecnicas', models.DO_NOTHING, db_column='Id_tecnica')  # Field name made lowercase.
    ruta_camara = models.TextField(db_column='Ruta_camara', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Planta'


class Tecnicas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre_de_metodo = models.CharField(db_column='Nombre de metodo', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recipiente = models.CharField(db_column='Recipiente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descipcion = models.CharField(db_column='Descipcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tecnicas'


class Usuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username')  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre')  # Field name made lowercase.
    apellidos = models.TextField(db_column='Apellidos', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    privilegios = models.IntegerField(db_column='Privilegios')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class UsuarioPlanta(models.Model):
    id_planta = models.ForeignKey(Planta, models.DO_NOTHING, db_column='id_Planta', blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_Usuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario_Planta'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
