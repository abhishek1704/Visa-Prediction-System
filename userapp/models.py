# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Applications(models.Model):
    app_id = models.CharField(primary_key=True, max_length=10)
    app_no = models.IntegerField(blank=True, null=True)
    dept = models.ForeignKey('Departments', models.DO_NOTHING, blank=True, null=True)
    corr_dept_name = models.CharField(max_length=20, blank=True, null=True)
    emp = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    security_ans = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Applications'


class CrbaApplication(models.Model):

    appl_no = models.AutoField(primary_key=True)
    childname = models.CharField(db_column='childName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=2, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    father_full_name = models.CharField(max_length=50, blank=True, null=True)
    fcontact = models.CharField(db_column='fContact', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fus_nat = models.CharField(db_column='fUS_Nat', max_length=2, blank=True, null=True)  # Field name made lowercase.
    mother_full_name = models.CharField(max_length=50, blank=True, null=True)
    mcontact = models.CharField(db_column='mContact', max_length=2, blank=True, null=True)  # Field name made lowercase.
    mus_nat = models.CharField(db_column='mUS_Nat', max_length=2, blank=True, null=True)  # Field name made lowercase.
    birth_loc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crba_application'


class Departments(models.Model):
    dept_id = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(max_length=20, blank=True, null=True)
    no_of_emp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=5)
    emp_fullname = models.CharField(max_length=30, blank=True, null=True)
    emp_emailid = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    corr_consulate_id = models.IntegerField(blank=True, null=True)
    consulate_name = models.CharField(max_length=20, blank=True, null=True)
    dept_id = models.CharField(max_length=2, blank=True, null=True)
    password = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Functionality(models.Model):
    func_id = models.IntegerField(primary_key=True)
    func_name = models.CharField(max_length=20, blank=True, null=True)
    dept_id = models.IntegerField(blank=True, null=True)
    corr_dept_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'functionality'


class H1BVisaApplication(models.Model):
    appl_no = models.AutoField(primary_key=True)
    ben_name = models.CharField(max_length=30, blank=True, null=True)
    ben_dob =  models.DateTimeField(blank=True, null=True)
    ben_gender = models.CharField(max_length=2, blank=True, null=True)
    ben_addr = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    job_title = models.CharField(max_length=20, blank=True, null=True)
    hrs_per_week = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    employer_name = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=20, blank=True, null=True)
    full_time_position = models.CharField(max_length=2, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h1b_visa_application'


class PassportRenewalApplication(models.Model):
    appl_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=12, blank=True, null=True)
    middle_name = models.CharField(max_length=12, blank=True, null=True)
    last_name = models.CharField(max_length=12, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    mailing_address = models.CharField(max_length=20, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    recent_passport_details = models.CharField(max_length=2, blank=True, null=True)
    occupation = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passport_renewal_application'


class TouristVisaApplication(models.Model):
    appl_no = models.AutoField(primary_key=True)
    app_fullname = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    natid = models.IntegerField(blank=True, null=True)
    addr = models.CharField(max_length=50, blank=True, null=True)
    travel_info = models.CharField(max_length=2, blank=True, null=True)
    passport_info = models.CharField(max_length=2, blank=True, null=True)
    criminal_activity = models.CharField(max_length=2, blank=True, null=True)
    country_of_origin = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tourist_visa_application'


class UserLogin(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login'
