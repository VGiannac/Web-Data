# xml_parser.py
import requests
import xml.etree.ElementTree as ET
import pandas as pd 

class XmlParser:
    """
    A class for parsing sitemap URLs from robots.txt and storing them in a DataFrame.

    Attributes:
    - robots_url (str): The URL of the robots.txt file containing sitemap information.
    """
    def __init__(self, robots_url):
    """
        Initialize the XmlParser with the URL of the robots.txt file.

        Parameters:
        - robots_url (str): The URL of the robots.txt file.
        """
        self.robots_url = robots_url

    def get_sitemap_urls(self):
    """
        Retrieve sitemap URLs from the robots.txt file.

        Returns:
        - list: A list of sitemap URLs.
        """
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
    """
        Retrieve and store sitemap URLs in a DataFrame.

        Returns:
        - pd.DataFrame: A DataFrame containing sitemap URLs.
        """
        # Get sitemap URLs
        sitemap_urls = self.get_sitemap_urls()

        # Create a DataFrame
        sitemap_df = pd.DataFrame({'Sitemap_URLs': sitemap_urls})

        return sitemap_df
