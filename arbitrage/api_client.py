import requests
from datetime import datetime
from .models import BettingOpportunity

def fetch_baseball_games():
    api_url = 'https://api.sportsdata.io/v3/mlb/scores/json/GamesByDate/{date}?key=2f4bf85ae1b54ac19bd30b1673b39ee5'  # Correct endpoint with API key
    api_key = '2f4bf85ae1b54ac19bd30b1673b39ee5'  # Replace with your actual API key

    # Fetch today's games
    today = datetime.today().strftime('%Y-%m-%d')
    url = api_url.format(date=today)
    
    headers = {
        'Ocp-Apim-Subscription-Key': api_key
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return
    
    data = response.json()
    
    for game in data:
        sport = 'Baseball'
        event = f"{game['HomeTeam']} vs {game['AwayTeam']}"
        bookmaker = 'SportsData.io'  # Replace with actual data if available
        odds = 1.0  # Replace with actual odds if available

        opportunity, created = BettingOpportunity.objects.get_or_create(
            sport=sport,
            event=event,
            bookmaker=bookmaker,
            defaults={'odds': odds, 'arbitrage_opportunity': True}
        )
        if not created:
            opportunity.odds = odds
            opportunity.save()
