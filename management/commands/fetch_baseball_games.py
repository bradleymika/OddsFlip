from django.core.management.base import BaseCommand
from arbitrage.api_client import fetch_baseball_games

class Command(BaseCommand):
    help = 'Fetch daily baseball games from SportsData.io API'

    def handle(self, *args, **options):
        fetch_baseball_games()
        self.stdout.write(self.style.SUCCESS('Successfully fetched baseball games'))
