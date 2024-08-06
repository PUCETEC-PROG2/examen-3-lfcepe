from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .models import Artist ,Album
from .forms import Artist_Form, Album_Form
def index(request):
    albums = Album.objects.order_by('album_title')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'albums': albums}, request))

def album(request, album_id):
    album = Album.objects.get(pk = album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def index_artist(request):
    artists = Artist.objects.order_by('artist_name')
    template = loader.get_template('index_artist.html')
    return HttpResponse(template.render({'artists': artists}, request))

def artist(request, artist_id):
    artist = Artist.objects.get(pk = artist_id)
    return render(request, 'display_artist.html', {'artist': artist})

#ADD POKEMON AND TRAINER
def add_artist(request):
    if request.method == 'POST':
        form = Artist_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index_artist')
    else:
        form = Artist_Form()
    
    return render(request, 'artist_form.html', {'form': form})

def add_album(request):
    if request.method == 'POST':
        form = Album_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = Album_Form()
        
    return render(request, 'album_form.html', {'form': form})

    
#EDIT POKEMON AND TRAINER
def edit_artist(request, id):
    artist = get_object_or_404(Artist, pk = id)
    if request.method == 'POST':
        form = Artist_Form(request.POST,request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index_artist')
    else:
        form = Artist_Form(instance=artist)
        
    return render(request, 'artist_form.html', {'form': form})

def edit_album(request, id):
    album = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = Album_Form(request.POST,request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = Album_Form(instance=album)
        
    return render(request, 'album_form.html', {'form': form})

#DELETE POKEMON AND TRAINER
def delete_artist(request, id):
    artist = get_object_or_404(Artist, pk = id)
    artist.delete()
    return redirect("album_manager:index_artist")

def delete_album(request, id):
    album = get_object_or_404(Album, pk = id)
    album.delete()
    return redirect("album_manager:index")