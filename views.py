from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')   
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')


        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        
        #return redirect('login')
    return render(request,'signup.html')        
def login(request):
    return render(request,'login.html')                     