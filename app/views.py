from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'topic.html',d)

def webpage(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.order_by('name')
    LWO=Webpage.objects.order_by('-name')
    LWO=Webpage.objects.order_by(Length('name'))
    LWO=Webpage.objects.order_by(Length('name').desc())
    d={'LWO':LWO}
    return render(request,'webpage.html',d)

def access(request):
    LAO=AccessRecords.objects.all()
    d={'LAO':LAO}
    return render(request,'access.html',d)