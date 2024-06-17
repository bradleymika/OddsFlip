from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, BettingOpportunity
from .forms import UserProfileForm
from datetime import datetime

@login_required
def dashboard(request):
    opportunities = BettingOpportunity.objects.filter(arbitrage_opportunity=True)
    return render(request, 'arbitrage/dashboard.html', {'opportunities': opportunities})

@login_required
def dashboard(request):
    today = datetime.today().date()
    opportunities = BettingOpportunity.objects.filter(created_at__date=today)
    return render(request, 'arbitrage/dashboard.html', {'opportunities': opportunities})

def home(request):
    return redirect('dashboard')

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'arbitrage/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'arbitrage/edit_profile.html', {'form': form})



