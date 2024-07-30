import scrapy


class QuotesspiderSpider(scrapy.Spider):
    name = "quotesSpider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        pass
