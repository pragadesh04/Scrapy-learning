from typing import Iterable


import scrapy

class CpSpider(scrapy.Spider):
    name = "CP"

    fn = "www.creepypasta"
    dn = fn + ".com"
    sorted = "/archive/top-ranked/"

    allowed_domains = [dn]
    start_urls = ["https://www.creepypasta.com" + sorted + "?_page=1"]
    scope = []
    for i in range (0,4):
        scope.append("https://"+ dn + sorted + "?_page=" + str(i))

    def start_requests(self):
        urls = self.start_urls + self.scope
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        div = response.css("._self.cvplbd::text").extract()
        with open("Creppies.txt" , 'a') as file:
            for i in range(len(div)):
                if div[i] == "Read Now":
                    continue
                else:
                    file.write(div[i] + "\n")
            file.write("\n\nPowered by www.CreepyPasta.com")
        pass
