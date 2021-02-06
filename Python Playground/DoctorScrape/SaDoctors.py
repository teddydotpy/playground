import bs4, requests

class ScrapeWeb:
    def __init__(self):
        self.Province_Area = []
        self.PageList = []

    def getPage(self, url):
        page = requests.get(url)
        page.raise_for_status()
        return page.text

    def setPageList(self, urlPAge, HtmlTag):
        soup_Parse = bs4.BeautifulSoup(urlPAge, "html.parser")
        self.PageList = soup_Parse.select(HtmlTag)

    def getPageList(self):
        return self.PageList
