from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import PostForm
from .models import Post
from volunteer.models import Application
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. Login below')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {'form': form})


def login(request):
    return render(request, 'user/login.html')

def userhome(request):
    return render(request, 'user/userhome.html')

@login_required
def applications(request):
    applications = Application.objects.filter(opportunity_creator=request.user)
    arg = {'apps': applications}
    return render(request, 'user/applications.html', arg)

def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            postform = post_form.save(commit=False)
            postform.save()
            messages.success(request, f'Opportunity created.')
            return redirect('userhome')
    else:
        post_form = PostForm()
    return render(request, 'user/create.html', {'form': post_form})

