from django.shortcuts import render

from Tkinter import *



def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'tracker/index.html', context_dict)


radio_var = IntVar()

radio_uno = Radiobutton(Main,text='Config1', value=1,variable = radio_var)
radio_due = Radiobutton(Main,text='Config2', value=2,variable = radio_var)
radio_tre = Radiobutton(Main,text='Config3', value=3,variable = radio_var)

if(which_button_is_selected == 1):
    #button1 code
elif(which_button_is_selected == 2):
    #button2 code
else(which_button_is_selected == 3):
    #button3 code