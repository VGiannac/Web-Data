import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.url = "https://finance.yahoo.com/news/"

    def get_html(self, url):
        response = requests.get(url)
        return response.text

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        news_titles = [title.text.strip() for title in soup.find_all('h3', class_='Mb(5px)')]
        news_summaries = [summary.text.strip() for summary in soup.find_all('p', class_='Fz(14px)')]
        
        return {
            'news_titles': news_titles,
            'news_summaries': news_summaries
        }

    def scrape_news(self):
        html = self.get_html(self.url)
        news_data = self.parse_html(html)
        return news_data 
