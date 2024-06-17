from django.contrib import admin
from .models import UserProfile, Subscription, BettingOpportunity, Transaction

admin.site.register(UserProfile)
admin.site.register(Subscription)
admin.site.register(BettingOpportunity)
admin.site.register(Transaction)
