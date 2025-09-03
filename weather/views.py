from django.shortcuts import render
from .services import weather_fetch

def home(request):
    weather_data = None
    if request.method == "POST":
        city = request.POST.get("city")
        weather_data = weather_fetch(city)
    
    return render(request, "weather/home.html", {"weather": weather_data})

