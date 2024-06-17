from django.test import TestCase
from .models import BettingOpportunity

class BettingOpportunityTest(TestCase):
    def setUp(self):
        BettingOpportunity.objects.create(sport="Football", event="Match 1", bookmaker="Bookmaker A", odds=1.5)

    def test_betting_opportunity_creation(self):
        opportunity = BettingOpportunity.objects.get(event="Match 1")
        self.assertEqual(opportunity.sport, "Football")
