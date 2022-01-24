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

        #Next page
        if('page' not in response.url) :url = '//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[58]/div/a[10]/@href'
        else:url = '//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[58]/div/a[10]/@href'.replace("a[10]", "a[11]")

        further_page_url = response.xpath(url).extract_first()
        complete_url_next_page = response.urljoin(further_page_url)
        yield scrapy.Request(complete_url_next_page)

