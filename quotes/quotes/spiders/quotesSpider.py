import scrapy

class QuotesspiderSpider(scrapy.Spider):
    name = "quotesSpider"
    fn = "quotes.toscrape"
    dn = fn + ".com"
    genre = ""
    allowed_domains = [dn]
    start_urls = ["https://quotes.toscrape.com" + genre + "/page/1"]
    # scope = [
    #     "https://" + dn + genre + "/page/2",
    #     # "https://" + dn + genre + "/page/3",
    #     # "https://" + dn + genre + "/page/4"
    # ]
    scope = []
    for i in range (0, 11):

        scope.append("https://" + dn + genre + "/page/"+str(i))

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
