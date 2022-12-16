
from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    dict = {}
    if (request.method == 'POST'):
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        myfile = request.POST.get('myfile')
        print("User name>>>>", uname)

        user_detail = UserDetail(
            user_name = uname,
            user_email = email,
            user_mobile = mobile,
            user_dob = birthday,
            user_gender = gender,
            user_myfile = myfile  
        )
        user_detail.save()

    dict = {}

    return render(request, 'index.html', context=dict)

def registration(request):

    dict1 = {}
    if(request.method == 'POST'):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        contact = request.POST.get('contact')
        mail = request.POST.get('mail')
        gendr = request.POST.get('gendr')
        dob = request.POST.get('dob')
        passwrd = request.POST.get('passwrd')

        user = User.objects.create_user(username=fname, password=passwrd)
        user.save()
        register = Registration(
            first_name = fname,
            last_name = lname,
            contact_no = contact,
            email_id = mail,
            gender = gendr,
            dob = dob,
            password = passwrd
        )
        register.fun(passwrd)



    # qs = Registration.objects.filter(first_name="rimal")
    # info = {'query_set': qs}
    # if qs:
    #     return render(request, 'registration.html', context=info)

    return render(request, 'registration.html', context=dict1)

@login_required(login_url='/signin')
def about(request):
    return render(request, 'about.html')

def signin(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        pasword = request.POST.get('pasword')
        user = authenticate(username= username, password= pasword )
        if user:
            login(request,user)
            return HttpResponse("Hello")
        else:
            return HttpResponse("Bye")

    return render(request, 'signin.html')

def logout_view(request):
    logout(request)

def result(request):

    dict2 = {}
    if (request.method == 'POST'):
        sname = request.POST.get('sname')
        rollno = request.POST.get('rollno')
        ftname = request.POST.get('ftname')
        pf = request.POST.get('pf')

        studentdetail = StudentDetail(
            student_name = sname,
            roll_no = rollno,
            father_name = ftname,
            pass_fail = pf
        )
        studentdetail.save()

        student = User.objects.create_user(username=sname, password=rollno)
        student.save()
        
    return render(request, 'result.html', context=dict2)

def student_login(request):
    if(request.method == 'POST'):
        ssname = request.POST.get('ssname')
        roll = request.POST.get('roll')

        student = StudentDetail.objects.filter(student_name = ssname, roll_no = roll)
        info ={'query_set': student}
        if student:
            return render(request, 'stud_data.html', context=info)

        else:
            info ={'query_set' : None}
            return render(request, 'stud_data.html', context=info)

    return render(request, 'student_login.html')

def change_user(request):
    if(request.method == 'POST'):
        ssname = request.POST.get('ssname')
        roll = request.POST.get('roll')
        newname = request.POST.get('newname')

        StudentDetail.objects.filter(student_name = ssname, roll_no = roll).delete()


    return render(request, 'changeuser.html')

def delete(request):
    roll = request.POST.get('roll')

    StudentDetail.objects.filter( roll_no = roll).delete()

    return render(request, 'student_login.html')

