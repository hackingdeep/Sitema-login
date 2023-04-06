from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def Bienvenido(request):
    return render(request,'bienvenido.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST.get('password2')
        user = User.objects.filter(username=username).exists()

        if user :
            return redirect('register')

        if password1 == password2:
            user = User.objects.create_user(username=request.POST['username'],
                                            password= request.POST['password1'])
            user.save()
            login(request,user)
            return redirect('bienvenido')
        
    else:
        return render(request,'register.html')




def IniciaSession(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = User.objects.filter(username=username).exists()

        if user:
            user = authenticate(request,username=username,password=password1,)
            login(request,user)
            return redirect('bienvenido')
        else:
            return redirect('register')
           
    else:
        return render(request,'login.html')
    

def deleteUser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')


@login_required(login_url='login')
def logou(request):
     logout(request)
     return redirect('/')