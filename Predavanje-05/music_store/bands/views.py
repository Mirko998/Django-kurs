from django.shortcuts import render
from .models import Band

# Create your views here.


def band_listing(request):
    """A view of all bands."""
    bands = Band.objects.all() # SELECT * FROM BANDS
    #first_band = Band.objects.first()
    #print(first_band)
    return render(request, 'bands/band_listing.html', {'bands': bands})

def band_detail(request, band_id):
    """A view of all band detail."""
    band = Band.objects.get(pk=band_id) # SELECT * FROM BANDS WHERE ID = band_id
    return render(request, 'bands/band_detail.html', {'band': band})

def band_search(request):
    """A view of all band detail."""
    queried_band = request.GET['q']
    print(queried_band)
    try:
        band = Band.objects.get(name=queried_band) # SELECT * FROM BANDS WHERE NAME = queried_band
        queried_band_exists = True

    except:
        queried_band_exists = False
    return render(request, 'bands/band_searched.html', {'band': band, 'results':queried_band_exists})
