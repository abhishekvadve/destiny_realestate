from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import *


def index(request):
    listings = Listings.objects.all()
    return render(request, 'index.html',{'listings':listings})


def detailed(request,list_id):
    listing = Listings.objects.get(pk=list_id)
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.listing = listing
                form.save()  # Save the form data to the Contact model
                return HttpResponse("Success")  # Redirect to a success page
    else:
        form = ContactForm(initial={'enquiry': listing})
    context = {
        'listing':listing,
        'form': form,
    }
    return render(request,'detail.html',context)

        
        



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Contact model
            return HttpResponse("Success")  # Redirect to a success page
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
