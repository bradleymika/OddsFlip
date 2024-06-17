from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

class BettingOpportunity(models.Model):
    sport = models.CharField(max_length=100)
    event = models.CharField(max_length=200)
    bookmaker = models.CharField(max_length=100)
    odds = models.FloatField()
    arbitrage_opportunity = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(BettingOpportunity, on_delete=models.CASCADE)
    amount = models.FloatField()
    profit = models.FloatField()
    transaction_date = models.DateTimeField(auto_now_add=True)
