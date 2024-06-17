from django.core.management.base import BaseCommand
from arbitrage.api_client import fetch_opportunities

class Command(BaseCommand):
    help = 'Fetch betting opportunities from API'

    def handle(self, *args, **options):
        fetch_opportunities()
        self.stdout.write(self.style.SUCCESS('Successfully fetched betting opportunities'))
