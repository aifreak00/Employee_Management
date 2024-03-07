from django.shortcuts import render
from django.http import HttpResponse
import datetime
def home(request):
    isActive=True
    if request.method=="POST":
      check=request.POST["check"]
      print(check)
      if check is None:isActive=False
      else: isActive=True
    date=datetime.datetime.now()
    isActive=True
    name="prathamesh"
    listofprg=[
        "even or odd",
        "palindrome",
        "prime"
    ]
    student={
        "student_name":"prathamesh",
        "student_college":"stems",
        "student_city":"solapur",
    }
    data={
        "date":date,
        "isActive":isActive,
        "name":name,
        "listofprg":listofprg,
        "student_data":student
    }
    print("test function is called from view")
    # return HttpResponse("<h1>hello this is index page</h1>"+str(date))
    return render(request,"home.html",data)
def about(request):
    # return HttpResponse("<h1>this is about page</h1>")  
    return render(request,"about.html",{})  
def services(request):
    # return HttpResponse("<h1>this is services page</h1>") 
    return render(request,"services.html",{})  
