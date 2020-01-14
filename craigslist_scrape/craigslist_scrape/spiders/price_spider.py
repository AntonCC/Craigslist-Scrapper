import scrapy
# to scrape pages:
# python3 scrapy crawl prices -o prices.json

class PriceSpider(scrapy.Spider):
    name = 'prices'

    # Change query variable to search for different items
    def start_requests(self):
        query = 'iphone'
        urls = [
            f'https://newyork.craigslist.org/search/sss?query={query}&sort=rel'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for item in response.css('li.result-row'):           
            yield {
                'title': item.css('.result-title::text')[0].get(),
                'price': item.css('.result-price::text')[0].get(),
                'link': item.css('.result-title::attr(href)').get()
            }
        
        next_page = response.css('a.button.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
    
