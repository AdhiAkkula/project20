from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

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
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(name__startswith='M')
    LWO=Webpage.objects.filter(name__endswith='i')
    LWO=Webpage.objects.filter(name__contains='sachin')
    LWO=Webpage.objects.filter(name__in='Neymar,MSD,sachin')
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'webpage.html',d)

def access(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date='1999-06-17')
    LAO=AccessRecords.objects.filter(date__year='1999')
    LAO=AccessRecords.objects.filter(date__month='06')
    LAO=AccessRecords.objects.filter(date__day='14')
    LAO=AccessRecords.objects.filter(date__year__gt='1999')
    LAO=AccessRecords.objects.filter(date__year__gte='1999')
    LAO=AccessRecords.objects.filter(date__year__lt='1999')
    LAO=AccessRecords.objects.filter(date__year__lte='1999')
    LAO=AccessRecords.objects.filter(Q(date__year='1999') & Q(date__day='17'))
    LAO=AccessRecords.objects.filter(Q(date__year='1999') | Q(date__day='14'))
    d={'LAO':LAO}
    return render(request,'access.html',d)