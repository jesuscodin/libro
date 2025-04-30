from django.shortcuts import render,redirect
from .models import list
from .forms import ContactForm


def homepage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:home')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def browse(request):
    return render(request, 'browse.html')

def explore(request):
    booklist = list.objects.all()
    return render(request, 'explore.html', {'lists': booklist})

def about(request):
    return render(request, 'about.html')