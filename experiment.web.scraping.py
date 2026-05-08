import requests
from bs4 import BeautifulSoup
import time


def scrape_website(url):
    """Download and parse a webpage."""
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def extract_table_rows(soup):
    """Find all rows in the table that have class 'even' or 'odd'."""
    selector = '#DataTables_Table_0'
    rows = soup.select(selector)
    return rows


def parse_table_row(row):
    """Extract country and total from a single table row."""
    cells = row.find_all('td')
    if len(cells) >= 2:
        country = cells[0].get_text(strip=True)
        total = cells[1].get_text(strip=True)
        return country, total
    return None, None


def display_table_data(rows):
    """Print the scraped table rows in a readable format."""
    if not rows:
        print('Keine passenden Tabellenzeilen gefunden.')
        return

    print('Gefundene Länder und Werte:')
    print('-' * 40)
    for i, row in enumerate(rows, start=1):
        country, total = parse_table_row(row)
        if country and total:
            print(f'{i}. {country} – {total}')
    print('-' * 40)
    print(f'Insgesamt {len(rows)} Zeilen gefunden.')


if __name__ == '__main__':
    target_url = 'https://www.floridamuseum.ufl.edu/shark-attacks/maps/world/'
    print(f'Scraping: {target_url}')
    print()

    soup = scrape_website(target_url)
    time.sleep(1)

    rows = extract_table_rows(soup)
    display_table_data(rows)
