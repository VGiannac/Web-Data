# xml_parser.py

import requests
import xml.etree.ElementTree as ET
import pandas as pd

class XmlParser:
    def __init__(self, robots_url):
        self.robots_url = robots_url

    def get_sitemap_urls(self):
        # Get content from robots.txt
        response = requests.get(self.robots_url)
        robots_content = response.text

        # To locate sitemap URLs, read robots.txt.
        sitemap_urls = []
        for line in robots_content.split('\n'):
            if line.startswith('Sitemap:'):
                sitemap_urls.append(line.split(': ')[1].strip())

        return sitemap_urls

    def get_sitemap_data(self):
        # Get sitemap URLs
        sitemap_urls = self.get_sitemap_urls()

        # Create a DataFrame
        sitemap_df = pd.DataFrame({'Sitemap_URLs': sitemap_urls})

        return sitemap_df


