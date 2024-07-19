import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

banner= "Made with Love By Utkarsh Aggarwal "
print(banner)

class Spider:
    def __init__(self):
        self.base_url = None
        self.visited_urls = set()
        self.internal_urls = set()
        self.external_urls = set()

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return bool(parsed.scheme) and bool(parsed.netloc)

    def get_links(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            return [link['href'] for link in links]
        except Exception as e:
            print(f"Error retrieving links from {url}: {e}")
            return []

    def crawl(self, url):
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        links = self.get_links(url)
        for link in links:
            full_url = urljoin(url, link)
            if self.is_valid_url(full_url):
                if self.base_url in full_url:
                    self.internal_urls.add(full_url)
                    self.crawl(full_url)
                else:
                    self.external_urls.add(full_url)

    def start(self):
        while True:
            self.base_url = input("Enter the base URL to spider (e.g., https://example.com): ")
            if self.base_url.strip():
                break

        self.crawl(self.base_url)
        print("Spidering complete.")
        print(f"Internal URLs found: {len(self.internal_urls)}")
        print(f"External URLs found: {len(self.external_urls)}")

        if self.external_urls:
            print("\nExternal URLs:")
            for url in self.external_urls:
                print(url)

# Usage example:
if __name__ == "__main__":
    spider = Spider()
    spider.start()
