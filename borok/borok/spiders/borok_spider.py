import scrapy

class PannonSpider(scrapy.Spider):
    name = 'pannon'
    start_urls = ['https://pannonbormivesceh.hu/hirek/']

    def parse(self, response):
        borok_div = response.css('div.raven-post')

        for bor in borok_div:
            yield{
                'nev' : bor.css('a.raven-post-title-link::text').extract(),
                'leiras' : bor.css('div.raven-post-excerpt::text').getall(),
                'kep' : bor.css('img::attr(src)').getall()
            }



