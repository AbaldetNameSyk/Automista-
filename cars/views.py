from django.shortcuts import render
from .models import Car

def bmw_page(request):
    return render(request, 'BMW.html')

def mers_page(request):
    return render(request, 'Mercedes-Benz.html')

def volks_page(request):
    return render(request, 'Volkswagen.html')

def ford_page(request):
    return render(request, 'Ford.html')

def audi_page(request):
    return render(request, 'audi.html')

def sko_page(request):
    return render(request, 'Skoda.html')

def niss_page(request):
    return render(request, 'Nissan.html')

def toyo_page(request):
    return render(request, 'Toyota.html')

def hyu_page(request):
    return render(request, 'Hyundai.html')

def hon_page(request):
    return render(request, 'Honda.html')

def chev_page(request):
    return render(request, 'Chevrolet.html')

def maz_page(request):
    return render(request, 'Mazda.html')

def cit_page(request):
    return render(request, 'Citroen.html')

def vol_page(request):
    return render(request, 'Volvo.html')

def fiat_page(request):
    return render(request, 'Fiat.html')

def lex_page(request):
    return render(request, 'Lexus.html')
def ren_page(request):
    return render(request, 'Renault.html')

def jeep_page(request):
    return render(request, 'Jeep.html')


def lr_page(request):
    return render(request, 'Land Rover.html')

def che_page(request):
    return render(request, 'Chery.html')

def dac_page(request):
    return render(request, 'Dacia.html')
def my_view(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'my_template.html', context)

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def AfterButton_page(request):
    return render(request, 'AfterButtonCar.html')

def Obrob_page(request):
    return render(request, 'ObrabotkaDannih.html')