import scrapy
from crawling.items import MovieItem
from scrapy.spiders import CrawlSpider


class RottenTomatoesSpider(CrawlSpider):

    name = 'rottentomatoes'
    allowed_domains = ['rottentomatoes.com']
    start_urls = ['https://www.rottentomatoes.com/top/bestofrt/?year=2018',]

    def parse(self, response):
        rows = response.xpath('//*[@class="table"]/tr/td[3]/a/@href').extract()
        for row in rows:
            link = 'https://www.rottentomatoes.com' + row
            yield scrapy.Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        i = MovieItem()
        i['title'] = response.css('h1.mop-ratings-wrap__title ::text').extract_first()
        i['critics_consensus'] = response.css('p.mop-ratings-wrap__text--concensus ::text').extract()
        i['average_grade'] = response.css('#js-rotten-count ::text').extract()[1]
        i['amount_reviews'] = response.css('.mop-ratings-wrap__text--small ::text').extract()[1]
        i['approval_percentage'] = response.css('.mop-ratings-wrap__percentage ::text').extract_first()
        i['image_urls'] = response.css('.posterImage ::attr(data-src)').extract()
        return i



