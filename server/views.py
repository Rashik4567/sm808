from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pyrebase


config = { 
  "apiKey": "AIzaSyCYZI9C2Fuc5bSM9R413RfIFR9a3TTecXM",
  "authDomain": "sim-808-31ef4.firebaseapp.com",
  "databaseURL": "https://sim-808-31ef4-default-rtdb.firebaseio.com",
  "projectId": "sim-808-31ef4",
  "storageBucket": "sim-808-31ef4.appspot.com",
  "messagingSenderId": "1005133719063",
  "appId": "1:1005133719063:web:21ef59d392d8d8d13c1e52",
  "measurementId": "G-3RPCF53RCM"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def access(request):
    context = {
        "lat":database.child('latitude').get().val(),
        "lon":database.child('lontitude').get().val()
    }
    print(context['lat'])
    print(context['lon'])
    return render(request, 'home.html', context=context)


@csrf_exempt
def update(request):
    if request.method == 'POST':
        lat = request.POST.get("lat")
        lon = request.POST.get("lon")

        database.update({"latitude":lat, "lontitude":lon})
    
    context = {
        "lat":database.child('latitude').get().val(),
        "lon":database.child('lontitude').get().val()
    }
    print(context['lat'])
    print(context['lon'])
    return render(request, 'home.html', context=context)

