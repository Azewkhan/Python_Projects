import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()

        sp = BeautifulSoup(html, "html.parser")

        for tag in sp.find_all("a"):
            url = tag.get("href")  # Links in html are contain in <a>href

            if url is None:
                continue

            if "stories" in url:                # Anything which has stories in it 
                print(self.site + url)


news = "https://news.google.com"
Scraper(news).scrape()