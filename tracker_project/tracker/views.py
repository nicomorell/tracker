from django.shortcuts import redirect

from django.shortcuts import render

from .forms import BMIForm, weightForm
import json

massJson = []
dayJson = []
test1 = []
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'tracker/index.html', context_dict)



def bmi(request):

    json1 = [11, 12, 13]
    user_input = json.dumps(json1)
    for x in json1:
        print(x)
    form = BMIForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save(commit=False)
        form.save()
        if (form.cleaned_data['weightKilos'] != None and form.cleaned_data['heightMetres'] != None):
            print "hello1"
            calc_bmi = (form.cleaned_data['weightKilos'] / form.cleaned_data['heightMetres']) / form.cleaned_data['heightMetres']
            return render(request, 'tracker/bmi.html', {'form': form, 'calc_bmi': calc_bmi, 'user_input': user_input})

        elif(form.cleaned_data['weightPounds'] != None and form.cleaned_data['heightFeet'] != None and form.cleaned_data['heightInches'] != None):
            print "hello2"
            heightImperial = ((form.cleaned_data['heightFeet'] * 12) + form.cleaned_data['heightInches'])
            heightImperial = heightImperial * heightImperial
            weightImperial = form.cleaned_data['weightPounds'] * 703
            calc_bmi = weightImperial / heightImperial
            return render(request, 'tracker/bmi.html', {'form': form, 'calc_bmi': calc_bmi, 'user_input': user_input})

        else:
            print "hello"
            return render(request, 'tracker/bmi.html', {'form': form, 'user_input': user_input})

    else:
        form = BMIForm()
        return render(request, 'tracker/bmi.html', {'form': form, 'user_input': user_input})

def weight(request):
    form = weightForm(request.POST)
    if request.method == "POST" and form.is_valid():
        print("hello")
        form.save()

        if massJson != [form.cleaned_data['mass']]:
            massJson.append(form.cleaned_data['mass'])
            dayJson.append(form.cleaned_data['day'])
            test1.append(form.cleaned_data['prevDay'])
            try:
                for x in dayJson:
                    print(x)
                    c = dayJson[x-1]
                    c = str(c)
                    print("dayJson is" + c)
                    b = massJson[x-1]
                    b = str(b)
                    print("massJson is" + b)
                    try:
                        if dayJson[x-1] == form.cleaned_data['prevDay'] and massJson[x-1] == form.cleaned_data['prevWeight']:
                           print(x-1)
                           print("Good")
                           dayJson[x-1] = form.cleaned_data['afterDay']
                           massJson[x-1] = form.cleaned_data['afterWeight']
                    except IndexError:
                        print(x)
                        print("BAD")
            except IndexError:
                print("doesn't exist")
                print(dayJson[0])



        mass1 = json.dumps(massJson)
        day1 = json.dumps(dayJson)

        return render(request, 'tracker/weight.html', {'form': form, 'mass1':mass1, 'day1' : day1})
    else:
        print("hello1")
        form = weightForm()
        return render(request, 'tracker/weight.html', {'form': form})

