from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Business, Neighbourhood,UserProfile,Post
from .forms import BusinessForm,PostForm




# Create your views here.

@login_required (login_url='/accounts/login/')
def index(request):
    neighborhoods = Neighbourhood.objects.all()

    return render(request, 'index.html', {'neighborhoods':neighborhoods})





@login_required (login_url='/accounts/login/')
def neighborhood(request, id):
    neighborhood = Neighbourhood.objects.get(id=id)
    current_user = request.user
    business = Business.objects.filter(neighbourhood=neighborhood)
    #posts = Post.objects.filter(hood=neighborhood)
    #posts = posts[::-1]
    posts = Post.objects.filter(neighborhood=neighborhood)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
             b_form = form.save(commit=False)
             b_form.neighbourhood = neighborhood
             b_form.user = current_user
             b_form.save()
             form = BusinessForm()
    else:
         form = BusinessForm()


    # if request.method == 'POST':
    #     postForm = PostForm(request.POST)
    #     if postForm.is_valid():
    #         p_form = form.save(commit=False)
    #         p_form.neighbourhood = neighborhood
    #         p_form.user = current_user
    #         p_form.save()
    #         postForm = PostForm()
    # else:
    #     postForm = PostForm()     


    # # params = {
    #     'posts': posts
    # }
    return render(request, 'neighborhood.html', {'neighborhood': neighborhood, 'form': form, 'business': business, 'postForm':form, 'posts': posts})



@login_required(login_url='/accounts/login/')
def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'

        return render(request, 'results.html', {'results':results, 'message': message})
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})



@login_required(login_url='/accounts/login/')
def post(request, id):
    neighborhood = Neighbourhood.objects.get(id=id)
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            p_form = form.save(commit=False)
            p_form.neighborhood = neighborhood
            p_form.user = current_user
            p_form.save()
            return redirect('neighborhood', neighborhood.id)
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form})    