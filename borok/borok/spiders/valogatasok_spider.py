import scrapy


class ValogatasokSpider(scrapy.Spider):
    name = "valogatasok"
    start_urls = ['https://www.bortarsasag.hu/hu/oktober#valogatasaink']

    def parse(self, response):
        posztok_div = response.css('div.sc-1yhxc1k-1')
        for poszt in posztok_div:
            poszt_kepe = poszt.css('div.sc-1yhxc1k-1 img::attr(src)').getall()
            poszt_neve = poszt.css('h3.sc-nnur69-0 span::text').getall()
            poszt_ara = poszt.css('div.sc-sxgpgl-17 span.sc-nnur69-0 ::text').getall()

            if not poszt_neve:
                continue
            yield {
                'nev': poszt_neve,
                'ar': poszt_ara,
                'kep': poszt_kepe
            }