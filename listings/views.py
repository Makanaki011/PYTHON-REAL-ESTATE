from django.shortcuts import render, redirect
from .models import Listings
from .forms import ListingForm


# Create your views here.
def listing_list(request):
    listings = Listings.objects.all()
    context = {"listings": listings}
    return render(request, "listings.html", context)

            #  retrieve or read

def listing_retrieve(request, pk):
    listing = Listings.objects.get(id=pk)
    context = {"listing": listing}

    return render(request, "listing.html", context)


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {"form": form}
    return render(request, "listing_create.html", context)


def listing_update(request, pk):
    testing = Listings.objects.get(id=pk)
    form = ListingForm(instance=testing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=testing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")    
    context = {"form": form}
    return render(request, "update.html", context)        
     



def listing_delete(request, pk):
    form= Listings.objects.get(id=pk)
    form.delete()
    return redirect("/")




    
