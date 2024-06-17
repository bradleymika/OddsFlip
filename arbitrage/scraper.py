import requests
from bs4 import BeautifulSoup
from .models import BettingOpportunity

def scrape_opportunities():
    url = 'http://example.com/betting-odds'  # Replace with the actual URL of the sports betting site
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example scraping logic
    for item in soup.select('.odds-item'):  # Replace with the actual CSS selector
        sport = item.select_one('.sport').text  # Replace with the actual CSS selector
        event = item.select_one('.event').text  # Replace with the actual CSS selector
        bookmaker = item.select_one('.bookmaker').text  # Replace with the actual CSS selector
        odds = float(item.select_one('.odds').text)  # Replace with the actual CSS selector

        opportunity, created = BettingOpportunity.objects.get_or_create(
            sport=sport,
            event=event,
            bookmaker=bookmaker,
            defaults={'odds': odds, 'arbitrage_opportunity': True}
        )
        if not created:
            opportunity.odds = odds
            opportunity.save()

