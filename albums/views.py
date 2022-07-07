from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Favorite
from .forms import AlbumForm, FavoriteForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    favorite_albums=[album for album in albums if album.check_is_user_favorite(request.user)] 
    return render(request, "Albums/list_albums.html", {"albums": albums, "favorite_albums": favorite_albums})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/add_album.html", {"form": form})


def view_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/view_album.html", {"album": album})


def edit_album(request,pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
    return render(request, "albums/delete_album.html", {"album": album})
    

def add_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    favorite = Favorite.objects.create(album=album, user=request.user)
    # create a favorite whose album we just got
    favorite.save()
    return redirect(to="list_albums",)


def undo_favorite(request, pk):
    favorite = Favorite.objects.get(album__id=pk)
    favorite.delete()
    return redirect(to="list_albums",)