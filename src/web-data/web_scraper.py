import requests
from bs4 import BeautifulSoup
import pandas as pd

class WebScraper:
    def __init__(self):
        self.base_url = "https://www.imdb.com/chart/top"

    def get_top_movies(self, num_movies=10):
        # Send a GET request to the IMDb top movies page
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information about the top-rated movies
        movie_elements = soup.select('td.titleColumn')
        movies = []

        for i, movie_elem in enumerate(movie_elements[:num_movies]):
            title = movie_elem.find('a').get_text(strip=True)
            year = movie_elem.find('span', class_='secondaryInfo').get_text(strip=True)
            rating = movie_elem.find_next('td').find('strong').get_text(strip=True)
            cast = self.get_cast_details(movie_elem.find('a')['href'])
            
            movies.append({
                'Rank': i + 1,
                'Title': title,
                'Year': year,
                'Rating': rating,
                'Cast': cast
            })

        return pd.DataFrame(movies)

    def get_cast_details(self, movie_url):
        # Get the cast details for a specific movie
        movie_url = f"https://www.imdb.com{movie_url}"
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        cast_list = []
        cast_elements = soup.select('td.primary_photo + td a[href^="/name/"]')
        
        for cast_elem in cast_elements:
            cast_list.append(cast_elem.get_text(strip=True))

        return ', '.join(cast_list)
