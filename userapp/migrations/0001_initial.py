# Generated by Django 2.2.3 on 2020-12-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('app_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('app_no', models.IntegerField(blank=True, null=True)),
                ('corr_dept_name', models.CharField(blank=True, max_length=20, null=True)),
                ('security_ans', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'Applications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CrbaApplication',
            fields=[
                ('appl_no', models.AutoField(primary_key=True, serialize=False)),
                ('childname', models.CharField(blank=True, db_column='childName', max_length=40, null=True)),
                ('sex', models.CharField(blank=True, max_length=2, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('father_full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('fcontact', models.CharField(blank=True, db_column='fContact', max_length=2, null=True)),
                ('fus_nat', models.CharField(blank=True, db_column='fUS_Nat', max_length=2, null=True)),
                ('mother_full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mcontact', models.CharField(blank=True, db_column='mContact', max_length=2, null=True)),
                ('mus_nat', models.CharField(blank=True, db_column='mUS_Nat', max_length=2, null=True)),
                ('birth_loc', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'crba_application',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(blank=True, max_length=20, null=True)),
                ('no_of_emp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('emp_fullname', models.CharField(blank=True, max_length=30, null=True)),
                ('emp_emailid', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('corr_consulate_id', models.IntegerField(blank=True, null=True)),
                ('consulate_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dept_id', models.CharField(blank=True, max_length=2, null=True)),
                ('password', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Functionality',
            fields=[
                ('func_id', models.IntegerField(primary_key=True, serialize=False)),
                ('func_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dept_id', models.IntegerField(blank=True, null=True)),
                ('corr_dept_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'functionality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='H1BVisaApplication',
            fields=[
                ('appl_no', models.AutoField(primary_key=True, serialize=False)),
                ('ben_name', models.CharField(blank=True, max_length=30, null=True)),
                ('ben_dob', models.DateField(blank=True, null=True)),
                ('ben_gender', models.CharField(blank=True, max_length=2, null=True)),
                ('ben_addr', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', models.CharField(blank=True, max_length=20, null=True)),
                ('job_title', models.CharField(blank=True, max_length=20, null=True)),
                ('hrs_per_week', models.IntegerField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=30, null=True)),
                ('occupation', models.CharField(blank=True, max_length=20, null=True)),
                ('full_time_position', models.CharField(blank=True, max_length=2, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'h1b_visa_application',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PassportRenewalApplication',
            fields=[
                ('appl_no', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=12, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=12, null=True)),
                ('last_name', models.CharField(blank=True, max_length=12, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, max_length=2, null=True)),
                ('mailing_address', models.CharField(blank=True, max_length=20, null=True)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('recent_passport_details', models.CharField(blank=True, max_length=2, null=True)),
                ('occupation', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'passport_renewal_application',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TouristVisaApplication',
            fields=[
                ('appl_no', models.AutoField(primary_key=True, serialize=False)),
                ('app_fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=2, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('natid', models.IntegerField(blank=True, null=True)),
                ('addr', models.CharField(blank=True, max_length=50, null=True)),
                ('travel_info', models.CharField(blank=True, max_length=2, null=True)),
                ('passport_info', models.CharField(blank=True, max_length=2, null=True)),
                ('criminal_activity', models.CharField(blank=True, max_length=2, null=True)),
                ('country_of_origin', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'tourist_visa_application',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'user_login',
                'managed': False,
            },
        ),
    ]