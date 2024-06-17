from django.core.management.base import BaseCommand
from arbitrage.scraper import scrape_opportunities

class Command(BaseCommand):
    help = 'Scrape betting opportunities'

    def handle(self, *args, **options):
        scrape_opportunities()
        self.stdout.write(self.style.SUCCESS('Successfully scraped betting opportunities'))
