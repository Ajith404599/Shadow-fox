# web_scraper.py

import requests
from bs4 import BeautifulSoup

# Target URL (demo site for testing scraping safely)
url = "https://quotes.toscrape.com"

try:
    response = requests.get(url)
    response.raise_for_status()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract quote texts and authors
    quotes = soup.find_all('div', class_='quote')

    print("📜 Quotes and Authors:\n")
    for i, quote in enumerate(quotes, start=1):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f"{i}. \"{text}\" — {author}")

except requests.exceptions.RequestException as e:
    print("Error occurred while fetching the webpage:", e)
