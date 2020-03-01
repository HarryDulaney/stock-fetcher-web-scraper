# @author HGDIV
from bs4 import BeautifulSoup
import requests

                        
print()
print()
print()
print("Welcome to Web Scraper Python!")
print("---------------------------------")
print("Please input the exact URL for the webpage you wish to scrap: ")

url = str(input())
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
print("Here are the id tags for: ")
print(url)
print("----------------------------------")
soup = soup.prettify()
tagslist = list(soup.children)
print(tagslist)

print("Input a tag from the list and I will scrape the values for you: ")
tag = str(input())
scrapeTag = list(soup.find_all(tag))

print(scrapeTag)

