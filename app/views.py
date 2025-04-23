from django.shortcuts import render
from app.models import Submit, Feedback ,Booking
# Create your views here.

def home(request):  
     if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        erno = request.POST.get('erno')
        problem = request.POST.get('problem')
        email = request.POST.get("email") 
        
        entry = Submit(name=name, phone=phone,problem=problem, email=email, erno=erno)
        entry.save()

        return render(request,'contactus_submited.html')  
      
     return render(request,'home.html')


def contactus(request):  
    return render(request,'contactus.html')

def aboutus(request):  
    return render(request,'aboutus.html')

def contactus_submited(request):
    return render(request,'contactus_submited.html')


def booking(request):
    if request.method=='POST':
        pickup_location  = request.POST.get('pickup')
        drop_location = request.POST.get('drop')
        phone = request.POST.get('phone')
        passengers = request.POST.get('passengers')
        pickup_time = request.POST.get('time')
        payment_amount = int(passengers) * 10
        entry = Booking(pickup_location =pickup_location , drop_location=drop_location,phone=phone,pickup_time=pickup_time,payment_amount=payment_amount,passengers=passengers)
        entry.save()

        return render(request,'bookingdone.html')


    return render(request,'booknowpage.html')

def booking_done(request):
    return render(request,'bookingdone.html')


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        suggestion = request.POST.get('suggestion')
        entry = Feedback(name=name, phone=phone,email=email,rating=rating,suggestion=suggestion)
        entry.save()

        return render(request, 'feedback_submit.html') 
    
    return render(request,'feedback.html')

def feedback_submit(request):
    return render(request, 'feedback_submit.html')