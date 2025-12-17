from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def bforms1(request):
    if request.method=='POST':
        form = modelContactform(request.POST)
        if form.is_valid():
            # name=form.cleaned_data['name']
            # email=form.cleaned_data['email']
            # message=form.cleaned_data['message']
            # data=Contact.objects.create(name=name,email=email,message=message)
            # data.save()
            form.save()
    else:
        form=modelContactform()
    return render(request,'form.html',{'form':form})