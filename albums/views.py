from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.
def list_albums(request):
    albums = Album.objects.all#.filter.all()#order_by('artist')
    return render(request, "albums/list_albums.html", {"albums": albums})


# def add_album(request):
#     if request.method == 'GET':
#         form = AlbumForm()
#     else:
#         form = AlbumForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_albums')
#     return render(request, "albums/add_album.html", {"form": form})


# def view_album()


# def edit_album()


# def delete_album()