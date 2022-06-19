from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Business, Neighbourhood,UserProfile,Post



# Create your views here.

@login_required (login_url='/accounts/login/')
def index(request):
    neighborhoods = Neighbourhood.objects.all()

    return render(request, 'index.html', {'neighborhoods':neighborhoods})