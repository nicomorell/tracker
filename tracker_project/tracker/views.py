from django.shortcuts import redirect

from django.shortcuts import render

from .forms import BMIForm


from Tkinter import *

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'tracker/index.html', context_dict)



def bmi(request):
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
             bmi = form.save(commit=False)
             bmi.author = request.user
             bmi.save()
             return redirect('index')
    else:
        form = BMIForm()
        return render(request, 'tracker/bmi.html', {'form': form})
