from fastapi import FastAPI, HTTPException
import httpx
from bs4 import BeautifulSoup
from typing import Dict

# Create a FastAPI app instance
app = FastAPI()

# Define the URL to scrape
MARKETWATCH_URL = "https://www.marketwatch.com/"

@app.get("/market-status", response_model=Dict)
async def get_market_status():
    # Perform web scraping of the market status page
    async with httpx.AsyncClient() as client:
        response = await client.get(MARKETWATCH_URL)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Could not retrieve market data")
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract relevant data - This is highly dependent on the website's structure
    try:
        # Example of extracting Dow, Nasdaq, S&P data - adjust selectors based on actual DOM structure
        dow = soup.select_one('.element--market-summary .cell--dow .quote .value').text
        nasdaq = soup.select_one('.element--market-summary .cell--comp .quote .value').text
        sp500 = soup.select_one('.element--market-summary .cell--spx .quote .value').text
    except AttributeError as e:
        raise HTTPException(status_code=500, detail="Error parsing market data")

    # Build a summarized data response
    market_status = {
        "Dow Jones": dow,
        "NASDAQ": nasdaq,
        "S&P 500": sp500,
    }

    return market_status

# Make sure to run this script with an ASGI server such as uvicorn
# e.g., uvicorn script_name:app --reload
