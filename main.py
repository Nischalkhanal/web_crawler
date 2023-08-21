import requests
from bs4 import BeautifulSoup


def product_Finder(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    source_code = requests.get(url, headers=headers)
    source_code.raise_for_status()  # Check for request errors
    plain_text = source_code.content  # Use .content for binary content like HTML
    soup = BeautifulSoup(plain_text, 'html.parser')
    links = soup.find_all('div', class_='b-info__title')  # Adjust the class name as needed
    print(f"Number of links found: {len(links)}")
    for link in links:
        print(link.get_text().strip())  # Use .get_text() to extract text content and .strip() to remove extra spaces


# Example URL from eBay's electronics category
url = 'https://www.ebay.com.au/b/Electronics/bn_7000259947'
product_Finder(url)