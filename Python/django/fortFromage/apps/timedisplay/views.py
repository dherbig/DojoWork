from django.shortcuts import render, HttpResponse
import datetime, time
# Create your views here.
def index(request):
    context = {
        "date": datetime.date.today(),
        "time": time.strftime("%X")
    }
    return render(request, 'timedisplay/index.html', context)
