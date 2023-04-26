from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Subscriber

# Create your views here.
def index(request):
    return render(request, 'kikoba/index.html')
 

def subscribe(request):
    if request.method == 'POST':
        # get the data 
        first_name = request.POST.get('first_name')
        department = request.POST.get('department')
        phone_number = request.POST.get('phone_number')

        #instantiate the object of the class 
        subscriber = Subscriber(first_name=first_name, department=department, phone_number=phone_number)

        #save the object to database
        subscriber.save()


        return HttpResponse('Thank for your Subscription')
        # return redirect ('')
    
    return render(request, 'kikoba/index.html')
