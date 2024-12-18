from fastapi.testclient import TestClient
from app import app  # Assuming your FastAPI app is in a file named app.py

client = TestClient(app)

def test_scrape_market_status():
    # Call the endpoint to get the market status
    response = client.get("/market-status")

    # Check if the request was successful
    assert response.status_code == 200

    # Validate the response content type
    assert response.headers['content-type'] == 'application/json'

    # Validate the structure of the JSON response
    market_data = response.json()
    assert 'status' in market_data
    assert 'major_indices' in market_data
    assert isinstance(market_data['status'], str)
    assert isinstance(market_data['major_indices'], dict)

    # Optionally, test for specific keys in `major_indices`
    expected_keys = ['Dow', 'Nasdaq', 'S&P 500']
    for key in expected_keys:
        assert key in market_data['major_indices']
        index_data = market_data['major_indices'][key]
        assert 'last' in index_data
        assert 'change' in index_data
        assert 'percent_change' in index_data