import requests
from bs4 import BeautifulSoup

url = input("Enter the URL to scrape: ")
filename = input("Enter the name of the output text file: ")

# Send a request to the URL and get the page HTML
response = requests.get(url)
html = response.content

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Find the data you want to extract from the HTML using Beautiful Soup's selectors
title = soup.select_one('h1').text
paragraphs = soup.select('p')

# Write the data to a text file
with open(filename, 'w', encoding='utf-8') as txtfile:
    txtfile.write(title + '\n\n')
    for p in paragraphs:
        txtfile.write(p.text + '\n\n')
        
print(f"Data has been extracted and saved to {filename}")
