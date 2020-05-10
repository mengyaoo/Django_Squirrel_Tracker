from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Sighting
from .form import SquirrelForm

def squirrel_id(request, squirrel_id):
    data = Sighting.objects.get(Unique_Squirrel_ID=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=data)
        if form.is_valid():
            form.save(commit=True)
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance=data)
    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)


def add(request):
    if request.method=="POST":
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings")
    else:
        form=SquirrelForm()
    context={
        'form':form,
            }
    return render(request,'sightings/edit.html',context)


def all_squirrels(request):

    squirrels= Sighting.objects.all()
    context={
            'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)


def stats(request):
    total_sites=Sighting.objects.count()
    Running_count=Sighting.objects.filter(Running=True).count()
    Chasing_count=Sighting.objects.filter(Chasing=True).count()
    Climbing_count=Sighting.objects.filter(Climbing=True).count()
    Eating_count=Sighting.objects.filter(Eating=True).count()
    Foraging_count=Sighting.objects.filter(Foraging=True).count()
    Kuks_count=Sighting.objects.filter(Kuks=True).count()
    Quaas_count=Sighting.objects.filter(Quaas=True).count()
    Moans_count=Sighting.objects.filter(Moans=True).count()
    context={
            "Total sites":total_sites,
            "Number of Running squirrels":Running_count,
            "Number of Chasing squirrels":Chasing_count,
            "Number of Climbing squirrels":Climbing_count,
            "Number of Eating squirrels":Eating_count,
            "Number of Foraging squirrels":Foraging_count,
            "Number of Kuks squirrels":Kuks_count,
            "Number of Quaas squirrels":Quaas_count,
            "Number of Moans squirrels":Moans_count,
    }
    return render(request,"sightings/stats.html",{'context':context})

def map (request):
    Squirrels = Sighting.objects.all()[:100]
    context = {
            'Squirrels': Squirrels
            }
    return render (request, 'sightings/map.html', context)
