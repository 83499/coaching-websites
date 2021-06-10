from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.shortcuts import redirect


from . models import Data_of_rows

def index(request):
     data = Data_of_rows.objects.all()
     n= len(data)
     params = {'range': range(1,n),'data': data}
     return render (request,"index.html" , params)

def index2(request):
     if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        username = request.POST["username"]
        if User.objects.filter(username = username).exists():
              messages.info(request, "username is taken , please try another username")
              return render (request,"create.html")
              
        elif User.objects.filter(email = email).exists():
             messages.info(request, "Email Address is taken , please try another email address")
             return render (request,"create.html")
        else:
            user = User.objects.create_user(username = username, password = password , email = email)
            user.last_name = lastname
            user.first_name = firstname
            user.save();
            return render (request,"success.html")
     else:
          return render (request,"create.html")
          
def index3(request):
     return render (request,"success.html")

def index4(request):
      if request.method == "POST":
         email = request.POST["email"]
         password = request.POST["password"]
         username = request.POST["username"]
         user = auth.authenticate(username = username , password = password )
        
         if user is not None:
              auth.login(request, user)
              return redirect("/")
         else:
               messages.info(request," Either Username or Password is  invalid")
               return render (request,"login.html")
      else:
            return render (request,"login.html")

def index5(request):
     auth.logout(request)
     return redirect("/")

def index6(request):
       return render (request,"maths9.html")


def index7(request):
       return render (request,"about_us.html")

