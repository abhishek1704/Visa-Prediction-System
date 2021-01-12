from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from userapp.models import Applications, H1BVisaApplication

ben_name = ""
ben_dob = ""
ben_gender = ""
ben_addr = ""
nationality = ""
job_title = ""
hrs_per_week = ""
salary = ""
employer_name = ""
occupation = ""
full_time_position = ""
location = ""
status = ""

def index(request):
    return render(request, 'userapp/home.html')

def visaForm(request):
    return redirect(reverse("h1bFirst"))

def h1bFirst(request):
    if request.method == 'POST':
        global ben_name, ben_gender, ben_dob, nationality
        fname = (request.POST.get('first_name'))
        mname = (request.POST.get('middle_name'))
        lname = (request.POST.get('last_name'))
        ben_name = " ".join([fname, mname, lname])
        ben_gender = request.POST.get('gender')
        ben_dob = str(request.POST.get('dob'))
        nationality = request.POST.get('nationality')

        d = ben_dob.split("/")[0]
        m = ben_dob.split("/")[1]
        y = ben_dob.split("/")[2]


        ben_dob = y + "-" + m + "-" + d
        print(str(ben_name) + " " + str(ben_dob) + " " + str(ben_dob) + " " + str(ben_gender))
        return redirect(reverse("h1bSecond"))
    else:
        return render(request, 'userapp/h1b_page1.html')

def h1bSecond(request):
    if request.method == 'POST':
        global employer_name, location
        employer_name = request.POST.get('name_org')
        location = request.POST.get('company_address')

        print(str(employer_name) + " " + str(location))
        return redirect(reverse("h1bSubmit"))
    else:
        return render(request, 'userapp/h1b_page2.html')

def h1bSubmit(request):
    global job_title, salary, full_time_position, status, occupation
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        salary = request.POST.get('salary')
        full_time_position = request.POST.get('fulltime')
        occupation = "COMPUTER PROGRAMMERS"

        print(str(job_title) + " " + str(salary) + " " + str(ben_name))
        status = getPredictions(employer_name, location, job_title, full_time_position, occupation, salary)

        if status == 'error':
            return HttpResponse("Something went wrong while predicting!")

        h1b_visa_app = H1BVisaApplication(ben_name=ben_name, ben_dob=ben_dob, ben_gender=ben_gender, ben_addr=ben_addr, nationality=nationality,
                                          job_title=job_title, hrs_per_week=60, salary=salary, employer_name=employer_name,
                                          occupation=occupation, full_time_position=full_time_position, location=location, status=status)
        h1b_visa_app.save()
        print(h1b_visa_app.status)
        return render(request, 'userapp/result.html', context={'status': status})
    else:
        return render(request, 'userapp/h1b_page3.html')


def DisplayApplications(request):
    all_apps = Applications.objects.all()

    for app in all_apps:
        print(app.app_id + " " + app.corr_dept_name)

    return render(request, 'userapp/temp.html', context={'all_apps': all_apps})


def getPredictions(employer_name, worksite, job_title, full_time_position, soc_name, salary):
    import pickle
    model = pickle.load(open("h1b_visa_status.sav", "rb"))

    cols = ['FULL_TIME_POSITION', 'PREVAILING_WAGE', 'YEAR', 'EMP_DELOITTE',
       'EMP_IBM', 'EMP_INFOSYS', 'EMP_OTHER', 'EMP_TCS', 'EMP_WIPRO', 'SOC_CO',
       'SOC_CP', 'SOC_CSA', 'SOC_OTHER', 'SOC_SDA', 'SOC_SDSS', 'JOB_CP',
       'JOB_OTHER', 'JOB_PA', 'JOB_SD', 'JOB_SE', 'JOB_SA', 'ATLANTA',
       'CHICAGO', 'HOUSTON', 'NY', 'OTHER', 'SAN_FRANSISCO']

    top_employers = ['DELOITTE', 'IBM', 'INFOSYS', 'TCS', 'WIPRO']
    top_soc = ['COMPUTER SYSTEMS ANALYSTS', 'SOFTWARE DEVELOPERS, APPLICATIONS','COMPUTER PROGRAMMERS',
                'COMPUTER OCCUPATIONS, ALL OTHER',
                'SOFTWARE DEVELOPERS, SYSTEMS SOFTWARE']
    top_worksite = ['NEW YORK, NEW YORK', 'HOUSTON, TEXAS', 'SAN FRANCISCO, CALIFORNIA', 'CHICAGO, ILLINOIS',
                    'ATLANTA, GEORGIA']
    top_jobtitle = ['OTHER', 'PROGRAMMER ANALYST', 'SOFTWARE ENGINEER', 'COMPUTER PROGRAMMER', 'SYSTEMS ANALYST']

    emp = get_vector(employer_name , top_employers)
    soc = get_vector(soc_name , top_soc)
    job = get_vector(job_title , top_jobtitle)
    workloc = get_vector(worksite , top_worksite)

    print(emp)
    print(soc)
    print(job)
    print(workloc)

    ftp = 0
    if full_time_position == 'Y':
        ftp = 1


    X = [[ftp, salary, 2015] + emp + soc + job + workloc]

    prediction = model.predict(X)
    print(prediction)
    if prediction == 0:
        return "Denied"
    elif prediction == 1:
        return "Certified"
    else:
        return "error"


def get_vector(name, top_val):
    i = 0
    L = [0, 0, 0, 0, 0]
    for val in top_val:
        if name.upper().find(val) != -1:
            L[i] += 1
            break
        i += 1

    if L.count(1) == 0:
        L.insert(3, 1)
    else:
        L.insert(3, 0)


    return L