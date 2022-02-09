import scrapy
from SRC.kijijiScraper.kijijiScraper import globalVar

class Spider1(scrapy.Spider):
    name = 'spider1'
    start_urls = [globalVar.urlToScrap]

    def parse(self, response):
        for product in response.css('div.info'):
            price = product.css('div.price::text').get().replace("\n", "").replace(" ", "").replace("\u00a0", "").replace("\u00c9", "").replace("$","")
            if(price != "Surdemande"):
                yield{
                    'price': price,
                }



        further_page_url = response.css("div.pagination > a:nth-last-child(2)::attr(href)").get()
        complete_url_next_page = response.urljoin(further_page_url)
        yield scrapy.Request(complete_url_next_page)

