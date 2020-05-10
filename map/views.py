from django.shortcuts import render
import sys,os,inspect
from sightings.models import squirrelsite


def index(reques):
    squirrels = squirrelsite.objects.all()
    sightings = squirrels[:100]
    context={
            'sightings':sightings,
            }
    return render(request,'map/map.html',context)
# Create your views here.
