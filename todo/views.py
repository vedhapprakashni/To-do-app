from django . shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODO
from django.contrib.auth import authenticate,login,logout


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken!'})

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()
        return redirect('/login')

    return render(request, 'signup.html')



def login_view(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/todo')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        latest_task = TODO.objects.filter(user=request.user).order_by('-user_task_id').first()
        next_task_id = latest_task.user_task_id + 1 if latest_task else 1

        obj = TODO(title=title, user=request.user, user_task_id=next_task_id)
        obj.save()

        user=request.user
        res=models.TODO.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo',{'res': res})
    res = models.TODO.objects.filter(user=request.user).order_by('-date')
    return render(request,'todo.html',{'res': res})  


def signout(request):
    logout(request)
    return redirect('login')

def edit_todo(request, srno):
    obj = TODO.objects.get(srno=srno)
    if request.method == 'POST':
        obj.title = request.POST.get('title')
        obj.save()
        return redirect('/todo')
    return render(request, 'edit_todo.html', {'obj': obj, 'user': request.user})
 

def todo_view(request):
    res = TODO.objects.all()
    return render(request, 'todo.html', {'res': res, 'user': request.user})
def delete_todo(request, srno):
    todo = TODO.objects.get(srno=srno)
    todo.delete()
    return redirect('/todo')
