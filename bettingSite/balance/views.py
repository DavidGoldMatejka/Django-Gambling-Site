from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def Deposit(request):
    return render(request, 'balance/deposit.html')

@login_required
def Withdraw(request):
    return render(request, 'balance/withdraw.html')