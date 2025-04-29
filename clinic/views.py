from django.shortcuts import  redirect, render
from django.contrib.auth.models import User
from .models import Appointment, Doctor,Patient,Reason,UserAppointment
from django.contrib.auth import authenticate, login,logout
from django.utils import timezone
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count 
# Create your views here.
def Home(request):
  return render(request,'home.html')

def About(request):
  return render(request,'about.html')

def Contact(request):
  return render(request,'contact.html')

def Index(request):
  if not request.user.is_staff:
    return redirect('login')
  doctors = Doctor.objects.all()
  patients = Patient.objects.all()
  appointment = Appointment.objects.all()
  d=0
  p=0
  a=0
  for i in doctors:
    d+=1
  for i in patients:
    p+=1
  for i in appointment:
    a+=1
  d1 = {'d': d, 'p': p, 'a': a}    
  
  return render(request,'index.html',d1)


def Login(request):
  error = ''
  if request.method == "POST":
    u = request.POST['uname']
    p = request.POST['pwd']
    user = authenticate(username=u, password=p)
    try:
     if user.is_staff:
      login(request, user)
      error = "no"
     else:
      error = "yes"
    except:
      error = "yes"
  d = {'error': error}
  return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('admin_login')

def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc =Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html',d)


def Delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor =Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')
  
def Add_Doctor(request):
  error = ''
  if not request.user.is_staff:
    return redirect('login')
  if request.method == "POST":
    n = request.POST['name']
    m = request.POST['mobile']
    sp = request.POST['specialization']
    e = request.POST['email']
    
    try:
     Doctor.objects.create(Name=n, Mobile=m, Specialization=sp, Email=e)
     error = "no"
    
    except:
      error = "yes"
  d = {'error': error}
  return render(request, 'add_doctor.html', d)

def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat =Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html',d)
  
  
def Add_patient(request):
  error = ''
  if not request.user.is_staff:
    return redirect('login')
  if request.method == "POST":
    name = request.POST['Name']
    mobile = request.POST['Mobile']
    age = request.POST['Age']
    gender = request.POST['gender']
    address = request.POST['Address']
    
    
    
    try:
     Patient.objects.create(Name=name, Mobile=mobile, Age=age,  gender=gender, Address=address )
     error = "no"
     return redirect('view_patient')
    
    except:
      error = "yes"
  d = {'error': error}
  return render(request, 'add_patient.html', d)



def Delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient =Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')
  
  
def View_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.all()
    d = {'app': app}
    return render(request, 'view_appointment.html',d)
  
  
def Add_appointment(request):
  error = ''
  if not request.user.is_staff:
    return redirect('login')
  doctor1 = Doctor.objects.all()
  patient1 = Patient.objects.all()
  if request.method == "POST":
    dname = request.POST['dname']
    pname = request.POST['pname']
    date = request.POST['date']
    time = request.POST['time']
    doctor= Doctor.objects.filter(Name=dname).first()
    patient= Patient.objects.filter(Name=pname).first()
    
    
    
    try:
     Appointment.objects.create(Doctor=doctor , Patient=patient, date=date,  time=time )
     error = "no"
     return redirect('view_appointment')
    
    except:
      error = "yes"
  d = {'doctor':doctor1,'patient': patient1, 'error': error }
  return render(request, 'add_appointment.html', d)



def Delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment =Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
  
  
  
  
def create_appointment(request):
    if request.method == 'POST':
        UserAppointment.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            dob=request.POST['dob'],
            reason_id=request.POST['reason'],
            details=request.POST['details'],
            appoint_date=request.POST['appoint_date'],
            time=request.POST['time'],
            doctor_id=request.POST['doctor']
        )
        return redirect('home')  # Redirect to a success page or home page
    
    reasons = Reason.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'form_appointment.html', {'reasons': reasons, 'doctors': doctors})