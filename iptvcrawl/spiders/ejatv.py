import scrapy


class EjatvSpider(scrapy.Spider):
    name = 'ejatv'
    allowed_domains = ['eja.tv']
    start_urls = [
        'https://eja.tv/?limit=0&country=cn&language=&category=&level=0&search=', 
        'https://eja.tv/?limit=0&country=hk&language=&category=&level=0&search=', 
        'https://eja.tv/?limit=0&country=mo&language=&category=&level=0&search=', 
        'https://eja.tv/?limit=0&country=tw&language=&category=&level=0&search=', 
        'https://eja.tv/?limit=0&country=jp&language=&category=&level=0&search=', 
        'https://eja.tv/?limit=0&country=us&language=&category=&level=0&search=',
    ]

    def parse(self, response):
        for card in response.css("#channelList .card"):
            attrs = card.css(".text-muted a::text").getall()
            link = card.css("span.cjs a::attr(href)").re(r"ejaCast\('(.+)',*'(.+)'\)")
            yield {"attrs": attrs, "link": link}
        next_page = response.xpath('//*[@id="pagination"]//i[contains(@class,"fa-arrow-alt-circle-right")]/../@href').get()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))
        
