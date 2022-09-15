import scrapy

class SzentAndreaSpider(scrapy.Spider):
    name = "szandrea"

    def start_requests(self):
        urls = ['https://www.bortarsasag.hu/hu/szeptember2022']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for news in response.css('div.sc-1yhxc1k-1'):
            yield\
                {
                'title' : news.css('h3 span::text').getall(),
                'ár' : news.css('s.sc-nnur69-0::text').getall(),
                'image' : news.css('div.sc-sxgpgl-10 img::attr(src)').getall(),
            }




