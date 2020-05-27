from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import View
from .models import RandomNumber

from random import randint
from datetime import datetime

def timestamp():
    ''' return current in seconds '''
    return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())

def generate_value():
    ''' generate random value between 0 and 100 '''
    return randint(0, 100)

def generate_next_update_time():
    ''' generate next value update time in seconds '''
    interval = randint(3, 10)  # seconds
    return timestamp() + interval

class HomePageView(View):
    template_name = "homepage.html"

    def get(self, request):
        print("getting")
        value = generate_value()
        next_update_time = generate_next_update_time()  # in seconds

        if RandomNumber.objects.count() == 0:
            # create object
            obj = RandomNumber.objects.create(pk=1)
        else:
            # if object already in database, use existing object
            obj = RandomNumber.objects.get(pk=1)

        obj.value = value
        obj.next_update_time = next_update_time
        obj.save()

        remaining_time = next_update_time - timestamp()
        return render(request, self.template_name, {'value': value, 'next': remaining_time})

def update(request):
    # generating random number between 0 and 100

    obj = RandomNumber.objects.get(pk=1)
    value = obj.value
    next_update_time = obj.next_update_time
    
    if timestamp() > next_update_time:
        print("updating value")
        value = generate_value()
        next_update_time = generate_next_update_time()  # in seconds

        # update object
        obj.value = value
        obj.next_update_time = next_update_time
        obj.save()

    remaining_time = next_update_time - timestamp()

    return JsonResponse({'value':value, 'next':remaining_time})
