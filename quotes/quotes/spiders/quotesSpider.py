import scrapy

class QuotesspiderSpider(scrapy.Spider):
    name = "quotesSpider"
    fn = "quotes.toscrape"
    dn = fn + ".com"
    allowed_domains = [dn]
    start_urls = ["https://quotes.toscrape.com/page/1"]
    scope = [
        "https://" + dn + "/page/2",
        "https://" + dn + "/page/3",
        "https://" + dn + "/page/4"
    ]

    def start_requests(self):
        urls = self.start_urls + self.scope
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        div = response.css(".quote")
        quotes = div.css(".text::text").extract()
        author = div.css(".author::text").extract()

        with open("quotes.txt", "a") as file:
            for i in range(len(quotes)):
                file.write(f"\n{quotes[i]}\n{author[i]}\n")

        yield {
            'quotes': quotes,
            'author': author,
        }
