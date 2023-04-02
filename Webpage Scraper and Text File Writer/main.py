import requests
from bs4 import BeautifulSoup

url = input("Enter the URL to scrape: ")
filename = input("Enter the name of the output text file: ")


response = requests.get(url)
html = response.content


response = requests.get(url)
html = response.content


soup = BeautifulSoup(html, 'html.parser')


title = soup.select_one('h1').text


paragraphs = soup.select('p')


with open(filename, 'w', encoding='utf-8') as txtfile:
    txtfile.write(title + '\n\n')
    for p in paragraphs:
        txtfile.write(p.text + '\n\n')
