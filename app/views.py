from django.shortcuts import render
from .forms import *

# Create your views here.
def bforms1(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
    else:
        form=ContactForm()
    return render(request,'form.html',{'form':form})