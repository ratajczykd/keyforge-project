from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def index(request):
    return render(request, 'index.html')

def players(request):
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

    return render(request, 'players.html', {'form': form})

def info(request):
    return render(request, 'info.html')
                    #context={"posilki":l})
