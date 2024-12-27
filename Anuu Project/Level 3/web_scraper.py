import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all quote elements on the page
        quotes = soup.find_all('div', class_='quote')
        
        # Extract and print quotes and authors
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            print(f"Quote: {text}\nAuthor: {author}\n")
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

# URL of the website to scrape
url = "http://quotes.toscrape.com/"
scrape_quotes(url)