from django.shortcuts import render
from django.http import HttpResponseRedirect
import random

from core.forms import NameForm
from core.models import Player

def index(request):
    return render(request, 'index.html')

def players(request):
    players = Player.objects.all()
    args = []
    for player in players:
        args.append(player.name)
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
    players = Player.objects.all()
    for i, player in enumerate(players):
        player.player_no = i
    pairs = []
    list_of_players = [i for i in range(1,len(players))]
    for i in range(1,len(players)):
        list_of_players.remove(i)
        pairs[0] = [i, random.choice(list_of_players)]


    return render(request, 'tournament.html', {'players':players})

def info(request):
    return render(request, 'info.html')
                    #context={"posilki":l})
