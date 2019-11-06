from django.shortcuts import render
from django.http import HttpResponseRedirect
import random

from core.forms import NameForm
from core.models import Player

def index(request):
    return render(request, 'index.html')

def players(request):
    names = Player.objects.all()
    args = []
    for name in names:
        args.append(name.name)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            # redirect to a new URL:
            return HttpResponseRedirect('/players/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'players.html', {'form': form, 'names':args})

def remove_players(request):
    Player.objects.all().delete()
    return HttpResponseRedirect('/players/')

def tournament(request):
    names = Player.objects.all()
    random.shuffle(names)
    return render(request, 'tournament.html', {'names':names})

def info(request):
    return render(request, 'info.html')
                    #context={"posilki":l})
