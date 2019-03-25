from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadDocument
from .models import Document


# def upload_document(request):

#     if request.method == 'POST':
#         form = UploadDocument(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             instance = Document(passport=request.FILES['passport'])
#             instance.save()
#             instance = Document(id_license=request.FILES['id_license'])
#             instance.save()
#             instance = Document(User=request.user)
#             instance.save()
#             # needs to add instance of User from cache
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadDocument()
#     return render(request, 'verification/verificate.html', {'form': form})


def upload_document(request):
    if request.method == 'POST':
        form = UploadDocument(request.POST, request.FILES)
        if form.is_valid():
            instance = Document()
            instance.passport = request.FILES['passport']
            instance.id_license = request.FILES['id_license']
            instance.user = request.user
            instance.save()

            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadDocument()
    return render(request, 'verification/verificate.html', {'form': form})

# Create your views here.
