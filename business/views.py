from django.shortcuts import render, redirect
from business.models import Business, Apartment, Tenant
# Create your views here.
def businesses(request):
    businesses = Business.objects.all().order_by("-created")

    context = {
        "businesses": businesses
    }
    return render(request, "business/businesses.html", context)


def new_business(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        postal_address = request.POST.get("postal_address")
        town = request.POST.get("town")
        county = request.POST.get("county")
        country = request.POST.get("country")

        Business.objects.create(
            name=name,
            phone_number=phone_number,
            postal_address=postal_address,
            town=town,
            county=county,
            country=country
        )

        return redirect("businesses")
    return render(request, "business/new_business.html")

def edit_business(request):
    if request.method == "POST":
        id = request.POST.get("business")
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        postal_address = request.POST.get("postal_address")
        town = request.POST.get("town")
        county = request.POST.get("county")
        country = request.POST.get("country")

        business = Business.objects.get(id=id)
        business.name = name
        business.phone_number = phone_number
        business.postal_address = postal_address
        business.town = town
        business.county = county
        business.country = country
        business.save()

        return redirect("businesses")
    return render(request, "business/edit_business.html")


def delete_business(request):
    if request.method == "POST":
        id = request.POST.get("business")
        business = Business.objects.get(id=id)
        business.delete()
        return redirect("businesses")
    return render(request, "business/delete_business.html")
