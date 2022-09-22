import scrapy


class SzentAndreaSpider(scrapy.Spider):
    name = "szandrea"
    start_urls = ["https://www.bortarsasag.hu/hu/szeptember2022"]

    def parse(self, response):
        borok_div = response.css('div.sc-1yhxc1k-1')
        for bor in borok_div:
            bor_neve = bor.css('h3 span::text').extract()
            bor_ara = bor.css('s.sc-nnur69-0::text').getall()
            bor_kepe = bor.css('div.sc-sxgpgl-10 img::attr(src)').getall()

            if not bor_neve:
                continue

            yield {
                'nev': bor_neve,
                'ar': bor_ara,
                'kep': bor_kepe
            }
