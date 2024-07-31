import scrapy


class QuotesspiderSpider(scrapy.Spider):
    name = "quotesSpider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        div = response.css(".quote")
        quotes = div.css(".text::text").extract()
        author = div.css(".author::text").extract()

        file = open("quotes.txt", "w")
        i = 0
        
        for t in quotes:
            file.write("\n" + t + "\n" + author[i] + '\n')
            i += 1

        yield{
            'quotes': quotes,
            'author': author,
        }
        pass
