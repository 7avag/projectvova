import csv
import requests
from bs4 import BeautifulSoup

def scrape_quotes(limit=100):
    quotes = []
    page = 1
    while len(quotes) < limit:
        url = f'http://quotes.toscrape.com/page/{page}/'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        quote_elements = soup.select('.quote')
        if not quote_elements:
            break
        for q in quote_elements:
            text = q.select_one('.text').get_text(strip=True)
            author = q.select_one('.author').get_text(strip=True)
            tags = [t.get_text(strip=True) for t in q.select('.tag')]
            quotes.append({'text': text, 'author': author, 'tag': tags[0] if tags else ''})
            if len(quotes) >= limit:
                break
        page += 1
    return quotes

if __name__ == '__main__':
    data = scrape_quotes(100)
    with open('../data/reviews.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['text', 'author', 'tag'])
        writer.writeheader()
        writer.writerows(data)
    print(f'Saved {len(data)} records to data/reviews.csv')