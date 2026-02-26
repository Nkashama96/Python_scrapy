import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL of the target website
url = "http://quotes.toscrape.com"

# Step 2: Fetch the HTML content from the URL
try:
    response = requests.get(url)
    # Raise an exception if the request was unsuccessful (e.g., 404 error)
    response.raise_for_status() 
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Step 3: Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

print(f"Website Title: {soup.title.text}\n")

# Step 4: Extract specific data (e.g., all quotes and authors)
# Find all elements with the tag 'span' and class 'text'
quotes = soup.find_all("span", class_="text")
# Find all elements with the tag 'small' and class 'author'
authors = soup.find_all("small", class_="author")

# Iterate over the extracted data and print it
for quote, author in zip(quotes, authors):
    print(f'"{quote.text.strip()}" - {author.text.strip()}')
