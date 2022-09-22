import scrapy

class SzentAndreaSpider(scrapy.Spider):
    name = "szandmagazin"
    start_urls = ["https://www.bortarsasag.hu/hu/magazin"]

    def parse(self, response):
        posztok_div = response.css('div.sc-b0f2so-0')
        for poszt in posztok_div:
            poszt_neve = poszt.css('a.sc-b0f2so-1').css("span::text").getall()
            poszt_tartalma = poszt.css('p.sc-nnur69-0::text').getall()
            poszt_kepe = poszt.css('div.sc-b0f2so-0 img::attr(src)').getall()
            if not poszt_neve:
                continue
            yield {
                'nev': poszt_neve,
                'tartalom': poszt_tartalma,#.replace(u'\xa0', u''),
                'kep': poszt_kepe
            }