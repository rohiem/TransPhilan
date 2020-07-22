from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe
from profiles.models import History

stripe.api_key = "sk_test_IuOGDfRGnLAtweFksrmP3RRM00hqU6j3VY"

# Create your views here.
def home(request):
	return render(request, 'pay/home.html')
@login_required
def index(request):
	return render(request, 'pay/pay.html')

@login_required
def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount=int(request.POST['amount'])
        history=History(user=request.user,amount=amount)

        history.save()
        customer=stripe.Customer.create(
			email=request.user.email,
			name=request.user.username,
			source=request.POST['stripeToken']
			)
			
        charge=stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency="usd",
			description="Donation",
			)

    return redirect(reverse('success', args=[amount]))

@login_required
def successMsg(request, args):
	amount = args
	return render(request, 'pay/success.html', {'amount':amount})
'''
@login_required
def pay(request):
    publishKey=settings.STRIPE_PUBLISHABLE_KEY
    if request.method=="POST":
        token=request.POST["stripetoken"]
        print(token)
        intent = stripe.PaymentIntent.create(
            amount=1099,
            currency='usd',
    # Verify your integration in this guide by including this parameter
            metadata={'integration_check': 'accept_a_payment'},
                )


    context={
        "publishKey":publishKey
    }
    return render(request,"pay/pay.html",context)
'''