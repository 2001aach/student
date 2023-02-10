from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from studentapp.forms import  studentform, markform
from studentapp.models import Login,addmarks

# Create your views here.

def mainpage(request):
    return render(request,'index.html')

def adminpage(request):
    return render(request,'index2.html')

def student(request):
    return render(request,'student.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_student:
                return redirect('student')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'loginpage.html')


def register(request):
    student_form=studentform()
    if request.method=='POST':
        student_form=studentform(request.POST,request.FILES)
        if student_form.is_valid():
            user=student_form.save(commit=False)
            user.is_student=True
            user.save()
            messages.info(request,'Registration Successfully')
            return redirect('loginpage')
    return render(request,'register.html',{'student_form':student_form})


def student_view(request):
    data= Login.objects.filter(is_student=True)
    return render(request,'stu_view.html',{'data':data})

def delete_student(request,id):
    d=Login.objects.get(id=id)
    if request.method=='POST':
        d.delete()
        return redirect("student_view")
    else:
        return redirect("student_view")




def update_student(request,id):
    data=Login.objects.get(id=id)
    stu=studentform(instance=data)
    if request.method=='POST':
        stu=studentform(request.POST or None,request.FILES or None,instance=data)
        if stu.is_valid():
            stu.save()
            return redirect('student_view')
    return render(request,'update_student.html',{'stu':stu})


def mark(request):
    form=markform
    if request.method=='POST':
        form=markform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mark_view')
    return render(request,'marks.html',{'form':form})

def mark_view(request):
    a = addmarks.objects.all()
    return render(request,'view_marks.html',{'a':a})

# def mark_view(request):
#     a=addmarks.objects.filter(stu=request.student)
#     return render(request, 'view_marks.html', {'a':a})


def mview(request):
    return render(request,'mview.html')

def student_profile(request):
    data = Login.objects.filter(is_student=True)
    return render(request,'profile.html',{'data':data})

def logout_view(request):
    logout(request)
    return redirect('loginpage')




