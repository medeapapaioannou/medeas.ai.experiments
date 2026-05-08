import requests 
from bs4 import BeautifulSoup
import time
def scrape_website(url = "https://www.floridamuseum.ufl.edu/shark-attacks/maps/world/"):
    response = requests.get(url = "https://www.floridamuseum.ufl.edu/shark-attacks/maps/world/")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
def extract_links_from_page(soup):
    all_links = soup.find_all('a')
    return all_links
def display_links(links):
    for i, link in enumerate(links[:10]):
        link_text = link.get_text(strip=True)
        link_url = link.get('href')
        print(f"{i+1}. {link_text}\n   URL: {link_url}\n")
if __name__ == "__main__":
    target_url = "https://www.floridamuseum.ufl.edu/shark-attacks/maps/world/"
    soup = scrape_website(target_url)
    links = extract_links_from_page(soup)
    display_links(links)