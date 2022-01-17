from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'City of Dreams'
    dest1.img = 'destination_1.jpg'
    dest1.price = 1050
    dest1.offer  = True

    dest2 = Destination()
    dest2.name = 'Kolkata'
    dest2.desc = 'City of Joy'
    dest2.img = 'destination_2.jpg'
    dest2.price = 950
    dest2.offer  = False

    dest3 = Destination()
    dest3.name = 'Jaipur'
    dest3.desc = 'The Pink City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 1000
    dest3.offer  = False

    dest4 = Destination()
    dest4.name = 'Banglore'
    dest4.desc = 'The IT HUB '
    dest4.img = 'destination_4.jpg'
    dest4.price = 1100
    dest4.offer  = False

    dest5 = Destination()
    dest5.name = 'Chennai'
    dest5.desc = 'The Tamil Capital'
    dest5.img = 'destination_5.jpg'
    dest5.price = 1050
    dest5.offer  = False

    dest6 = Destination()
    dest6.name = 'Delhi'
    dest6.desc = 'The National Capital'
    dest6.img = 'destination_6.jpg'
    dest6.price = 1000
    dest6.offer  = False

    dests = [dest1,dest2,dest3,dest4,dest5,dest6]

    return render(request, 'index.html', {'dests':dests})