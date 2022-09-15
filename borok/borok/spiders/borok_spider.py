import scrapy

class BorokSpider(scrapy.Spider):
    name = "borok"

    def start_requests(self):
        urls = ['https://pannonbormivesceh.hu/hirek/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for news in response.css('div.raven-post'):
            yield\
                {
                'title' : news.css('a.raven-post-title-link::text').getall(),
                'content' : news.css('div.raven-post-excerpt::text').getall(),
                'image' : news.css('img::attr(src)').getall(),
            }




