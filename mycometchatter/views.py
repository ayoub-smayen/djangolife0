from django.shortcuts import render

# Create your views here.
def band_listing(request):
    """A view of all bands."""

    return render(request, 'chatter/index.html')



def band_listing2(request):
    """A view of all bands."""

    return render(request, 'chatter/login.html')