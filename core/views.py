from django.shortcuts import render
from django.views import View
import folium
# Create your views here.
class IndexView(View):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        # create map object
        m = folium.Map()
        # get html representation of map
        m = m._repr_html_()
        context = {
            "m":m
        }
        return render(request,self.template_name, context)