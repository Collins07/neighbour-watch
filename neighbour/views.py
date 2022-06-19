from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Business, Neighbourhood,UserProfile,Post



# Create your views here.

@login_required (login_url='/accounts/login/')
def index(request):
    neighborhoods = Neighbourhood.objects.all()

    return render(request, 'index.html', {'neighborhoods':neighborhoods})





@login_required (login_url='/accounts/login/')
def neighborhood(request, id):
    neighborhood = Neighbourhood.objects.get(id=id)
    #business = Business.objects.filter(neighbourhood=neighborhood)
    #posts = Post.objects.filter(hood=neighborhood)
    #posts = posts[::-1]
    # if request.method == 'POST':
    #     form = BusinessForm(request.POST)
    #     if form.is_valid():
    #         b_form = form.save(commit=False)
    #         b_form.neighbourhood = hood
    #         b_form.user = request.user.profile
    #         b_form.save()
    #         return redirect('single-hood', hood.id)
    # else:
    #     form = BusinessForm()
    # # params = {
    #     ,
    #     'business': business,
    #     'form': form,
    #     'posts': posts
    # }
    return render(request, 'neighborhood.html', {'neighborhood': neighborhood})