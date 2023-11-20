# xml_parser.py

import requests
import xml.etree.ElementTree as ET
import pandas as pd

class XmlParser:
    def __init__(self, robots_url):
        self.robots_url = robots_url

    def get_sitemap_urls(self):
        # Fetch robots.txt content
        response = requests.get(self.robots_url)
        robots_content = response.text

        # Parse robots.txt to find sitemap URLs
        sitemap_urls = []
        for line in robots_content.split('\n'):
            if line.startswith('Sitemap:'):
                sitemap_urls.append(line.split(': ')[1].strip())

        return sitemap_urls



