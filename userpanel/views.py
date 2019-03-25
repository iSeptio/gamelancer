from django.shortcuts import render
from .forms import profileForm
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'userpanel/index.html')


def profile_settings(request):
    if request.method == 'POST':
        form = profileForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = profileForm(instance=request.user)
        return render(request, 'userpanel/profilepicture.html', {'form': form})
