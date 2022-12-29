from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

import folium
import geocoder

from core.models import Search
# Create your views here.
def IndexView(request):
    template_name = "index.html"    
    q = request.GET.get("q")
    address = q
    if address is None:
        address = "Kathamndu"
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    # create map object
    m = folium.Map(location=[19,-12], zoom_start=2)
    try:
        folium.Marker([lat,lng], tooltip="click for more", popup=country).add_to(m)
        m = m._repr_html_()
    except ValueError:
        messages.error(request, "Location not found")
    # get html representation of map
    context = {
        "m":m,
        }
    return render(request,template_name, context)