from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import random
from users.models import Profile
from django.db.models import F
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal



# Create your views here.

def Home(request):
    return render(request, 'bets/bets.html')



def Cards(request):
    return render(request, 'bets/cards.html')


#@login_required
#def Red(request, winner):
    #profile = get_object_or_404(Profile, user=request.user)
    #profile.coins += 10
    #profile.save(update_fields=['coins'])
    #winner = random.randrange(11)
    #return HttpResponse('') #essentially returning void

    

# need to have a line of code in javascript that sets user.profile.coins to a integer, then tests if the amount from that input field is less 
# then user.profile.coins and that amount isn't negative, only then can the decrement function be called. 
# proces in decrement is just a failsafe


@api_view(['POST'])
def Decrement(request):
    amount = request.data['amount']
    amount = Decimal(amount)
    profile = get_object_or_404(Profile, user=request.user)
    print(profile)
    if(amount <= profile.coins):
        profile.coins -= amount
        profile.save(update_fields=['coins'])
    else:
        return Http404("Decrementing by more than total coins")
    return Response({"message": "Got some data!", "data": request.data})


#def Increment(request):
    #if request.method=="GET":
        #amount = request.GET.get('amount', 0) # returns 5
        #persist = request.GET.get('persist', 'no') #returns yes
        #profile = get_object_or_404(Profile, user=request.user)
        #profile.coins += amount
        #profile.save(update_fields=['coins'])

    #return HttpResponse('') #return void


@api_view(['POST'])
def Increment(request):
    amount = request.data['amount']
    amount = Decimal(amount)
    profile = get_object_or_404(Profile, user=request.user)
    print(profile)
    profile.coins += amount
    profile.save(update_fields=['coins'])
    return Response({"data": request.data})


@api_view(['GET'])
def getCoins(request):
    profile = get_object_or_404(Profile, user=request.user)
    return Response({"coins": profile.coins})
   