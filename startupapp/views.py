from django.shortcuts import render,redirect
from django.http import HttpResponse
from authapp.models import Contact
from django.contrib import messages
from startupapp.models import Courses,Trainer,Registration,Payment,Attendance
from .forms import registraionForm
from django.contrib.auth import authenticate
from django.views import View
from django.core.mail import send_mail



# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        des = request.POST['message']
        try:
            contact_data = Contact(name=name, Email=email, phone= phone, des= des)
            contact_data.save()
            messages.success(request, "Thanks for contact us. We will contact with you.")
            
        except:
            pass
       
        return render(request, 'contact.html')

        
    return render(request, 'contact.html')

def courses(request):
    course_list = Courses.objects.all()
    if request.method=='GET':
        st=request.GET.get('search_item')
        if st:
            course_list = Courses.objects.filter(courseName__icontains=st)
            return render(request, "search.html", {'courses':course_list})
            
        
        
    return render(request, "courses.html",{'courses':course_list})
def course(request,id):
    course = Courses.objects.filter(courseName=id)
    return render(request, "coursedetails.html", {'course':course})


def enroll(request):
    courses = Courses.objects.all()
    trainers=Trainer.objects.all()
    context = {'courses':courses,'trainers':trainers}
    if request.method=='POST':
        if not request.user.is_authenticated:
            messages.warning(request,"Please Login With us")
            return redirect("/auth/login/")
        
    
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        fathername = request.POST.get('fathername')
        fathername = request.POST.get('fathername')
        phonenumber = request.POST.get('phonenumber')
        alternetphonenumber = request.POST.get('alternetphonenumber')
        college = request.POST.get('college')
        address = request.POST.get('address')
        street = request.POST.get('street')
        landmark = request.POST.get('landmark')
        pincode = request.POST.get('pincode')
        qualification = request.POST.get('qualifaction')
        scourse = request.POST.get('scourse')
        trainer = request.POST.get('trainer')
    
        confirmcourse = request.POST.get('ccourse')
        trainer = Trainer.objects.get(trainer_name=trainer)
        email = request.POST['useremail']
        if scourse==confirmcourse:
            obj=Registration(email=email,fname=firstname,lname=lastname,father_name=fathername,phoneNumber=phonenumber,alternetPhoneNumber=alternetphonenumber,collegename=college,address=address,street=street,landmark=landmark,pincode=pincode,qualifaction=qualification,course=scourse,trainer=trainer)
            obj.save()
            messages.success(request,"Register successfully")
            return redirect("/profile/")
        else:
            messages.error(request,"Select a valid course")
            return redirect("/enroll/")
        
        
        
    return render(request, "enroll.html",context)


def profile(request):
    context={}
    if request.user.is_authenticated:
        try:
            condidate = Registration.objects.get(email=request.user.email)
            attendence = Attendance.objects.filter(student=condidate.condidateId)
            print(attendence)
            paymentstatus = Payment.objects.all()
            print(condidate)
            context={'obj':condidate, 'attendences':attendence}
        except:
            pass
        
        return render(request,'profile.html',context)
        
    
        
    return render(request,'profile.html')


def profileUpdate(request,id):
    data = Registration.objects.get(condidateId=id)
    courses=Courses.objects.all()
    context = {'data':data, 'courses':courses}
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        fathername = request.POST.get('fathername')
        fathername = request.POST.get('fathername')
        phonenumber = request.POST.get('phonenumber')
        alternetphonenumber = request.POST.get('alternetphonenumber')
        college = request.POST.get('college')
        address = request.POST.get('address')
        street = request.POST.get('street')
        landmark = request.POST.get('landmark')
        pincode = request.POST.get('pincode')
        qualification = request.POST.get('qualifaction')
        scourse = request.POST.get('scourse')
        confirmcourse = request.POST.get('ccourse')
        if scourse==confirmcourse:
            data.fname = firstname
            data.lname = lastname
            data.father_name=fathername
            data.phoneNumber = phonenumber
            data.alternetPhoneNumber=alternetphonenumber
            data.collegename=college
            data.address=address
            data.street=street
            data.landmark=landmark
            data.pincode=pincode
            data.qualifaction=qualification
            data.course=confirmcourse
            data.save()
            
            messages.success(request,"Details updated successfully")
            return redirect("/profile/")
        
        
    return render(request, "profileupdate.html",context)

def attendence(request):
    # reg = Registration()
    # data = Attendance.objects.get(student=reg.condidateId)
    # context={'data':data}
    # print(context)
    
    return render(request,"attendence.html")

class RequestResetPassword(View):
    def get(self,request):
        return render(request, "resetpassword.html")
    
    
    
    