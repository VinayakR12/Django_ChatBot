from django.contrib.auth.models import User, auth
from .models import Book
from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse

def login(request):
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/first?name={}'.format(name))
            # return HttpResponse("login Sussessfully Next..")
            # context = {'name':name}
            # return redirect('/first', {'name':name})


    return render(request,'login.html')
    # return HttpResponse('login sucessfully')

def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email = request.POST['email']
        password = request.POST['pass']
        data=User.objects.create_user(username=name,first_name=name,last_name=phone,email=email,password=password)
        data.save()
        return redirect('/login')
        # return HttpResponse("<h1>Register Successfully.....</h1>")
        # return redirect(reverse('login'))

    return render(request, 'register.html')
    # return HttpResponse('signup sucessfully')

def first(request):
    name = request.GET.get('name')
    def hellow(self):
        vin=22+909
        return vin
    hell = hellow('self')

    if request.method=="POST":
        data =request.POST
        use =data.get("name11")
        source =data.get('source')
        destination =data.get('destination')
        seatType =data.get('seatType')
        Book.objects.create(name=use,source=source,destination=destination,seatType=seatType)
        success=HttpResponse()
        success.write('<script>alert("Your Response Successfully Recorded...");</script>')
        success.write("<script> var urlParams = new URLSearchParams(window.location.search); var user = urlParams.get('name');window.location.href=`/first?name=${user}`;</script>")
        return success
    queryset = Book.objects.all()
    context = {'result': hell,'data':queryset}
    return render(request,'first.html',context)

def delete(request,id):
    rem = Book.objects.get(id = id)
    rem.delete()
    return HttpResponse("Ticket Deleted Successfully.....")

def api(request):
    return render(request,'schedule.html')


# def home(request):
#     url = "https://irctc1.p.rapidapi.com/api/v1/checkSeatAvailability"
#
#     querystring = {"classType": "2A", "fromStationCode": "ST", "quota": "GN", "toStationCode": "BVI",
#                    "trainNo": "19038", "date": "<REQUIRED>"}
#
#     headers = {
#         "X-RapidAPI-Key": "f1466b1727msh0c4cb5fd390cc29p1abca3jsn25c358365e4",
#         "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
#     }
#
#     response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())
    #
    # return HttpResponse("API")
