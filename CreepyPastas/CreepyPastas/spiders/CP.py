from typing import Iterable
import time

import scrapy

class CpSpider(scrapy.Spider):
    name = "CP"

    fn = "www.creepypasta"
    dn = fn + ".com"
    sorted = "/archive/top-ranked/"

    allowed_domains = [dn]
    # start_urls = ["https://www.creepypasta.com" + sorted + "?_page=1"]
    scope = []
    for i in range (1,2):
        scope.append("https://"+ dn + sorted + "?_page=" + str(i))

    def start_requests(self):
        time.sleep(0.05)
        urls =self.scope
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        # div = response.css("._self.cvplbd::text").extract()
        div = response.css(".pt-cv-ifield")
        title = div.css("._self.cvplbd img::attr(alt)").extract()
        links = div.css(".pt-cv-href-thumbnail::attr(href)").extract()
        rating = div.css(".pt-cv-ctf-value::text").extract()

        with open("Creppies.txt" , 'a') as file:
            for i in range(len(title)):
                file.write("Title:" + title[i] + "\n")
                file.write("Links: " + links[i] + "\n" + f"Average Rating: {rating[i]}".center(len(links[i])+7, "-") + "\n\n")

        yield{
            "div" : div,
            "title": title,
            "links": links
        }
        pass
