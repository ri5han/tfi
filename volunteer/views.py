from django.shortcuts import render, redirect
from volunteer.models import Application
from user.models import Post
from django.contrib import messages
from .forms import ApplicationForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    args = {'posts': posts}
    return render(request, 'volunteer/home.html', args)

def apply(request):
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            appform = application_form.save(commit=False)
            appform.save()
            messages.success(request, f'Your application is sent.')
            return redirect('home')
    else:
        application_form = ApplicationForm()

    return render(request, 'volunteer/apply.html', {'form': application_form})
