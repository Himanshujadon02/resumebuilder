from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Resume
from .forms import ResumeForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def basepage(request):
    return render(request,'base.html')

class AddClient(View):
    def get(self,request):
        form=ResumeForm()
        candidates = Resume.objects.all()
        return render(request,'addclient.html',{'candidates':candidates ,'form':form})

    def post(self,request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return render(request,'addclient.html',{'form':form})
            return redirect("addclient")

class CandidateView(View):
    def get(self,request,pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request,'candidate.html',{'candidate':candidate})

def signpage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse('your password and confirmed password are not same')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return  redirect('login')
        
    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')


def homepage(request):
    return render(request,'home.html')


#this function will update and edit
def edit_data(request,id):
    if request.method == "POST":
        pi=Resume.objects.get(pk=id)
        form = ResumeForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi=Resume.objects.get(pk=id)
        form = ResumeForm(request.POST,instance=pi)
    return render(request,'edit.html',{'form':form})

#this function will delete
def delete_data(request,id):
    if request.method=='POST':
        pi =Resume.objects.get(pk=id)
        pi.delete()
        return redirect('addclient')

def addeducation(request):
    candidates = Resume.objects.all()
    return render(request,'education.html',{'candidates':candidates})