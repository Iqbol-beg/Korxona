from django.shortcuts import render,redirect
from .import models

# Create your views here.


# front
def index(request):
    services =models.Service.objects.all()
    activities = models.Activitie.objects.all()
    ourblogs =models.Ourblog.objects.all()
    contacts = models.Contact.objects.all()
    context = {
        'services' :services,
        'activities' : activities,
        'ourblogs' : ourblogs,
        'contacts' : contacts
    }
    return render(request, 'index.html', context)

def services(request):
    context ={
       'services' :models.Service.objects.all()
    }
    
    return render(request, 'front/services.html', context)


def activities(request):
    context = {
     'activities' :models.Activitie.objects.all()
    }
    
    return render(request, 'index.html', context)



def ourblogs(request):

    context = {
        'ourblogs' :models.Ourblog.objects.all()
    }
    return render(request, 'front/blog.html', context)

def partners(request):
    context = {
        'partners' :models.Partner.objects.all()

    }
    return render(request, 'front/blog.html', context)

# xabar yuborish
def contacts(request):
    if request.method == 'POST':
        models.Contact.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            message=request.POST['message']
        )
    
    contacts = models.Contact.objects.all()
    
    context = {
        'contacts': contacts
    }
   
    return render(request, 'front/contact.html', context)