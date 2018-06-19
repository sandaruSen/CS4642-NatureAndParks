import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c57-t95-Sri_Lanka.html',
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c61-t52-Sri_Lanka.html',
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c57-t162-Sri_Lanka.html',
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c57-t66,162-Sri_Lanka.html',
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c57-t67-Sri_Lanka.html',
        'https://www.tripadvisor.com/Attractions-g293961-Activities-c57-t58-Sri_Lanka.html'
    ]

    def parse_details(self, response):

        yield {
            'title': response.css('h1.heading_title::text').extract()[0],
            'category': response.css('div.detail a::text').extract()[0],
            'tagWords': response.css('div.tagWord::text').extract(),
            'phone':response.css('div.detail_section.phone::text').extract_first(),
            'rating': response.css('span.overallRating::text').extract()[0],
            'streetAddress': response.css('span.street-address::text').extract_first(),
            'extendedAddress': response.css('span.extended-address::text').extract_first(),
            'locality': response.css('span.locality::text').extract_first(),
            'nearbyPlaces': response.css('div.poiName::text').extract(),
            'reviewType': response.css('span.row_label.row_cell::text').extract(),
            'reviewAmount': response.css('span.row_count.row_cell::text').extract(),

        }

    def parse(self, response):

        places = response.xpath('//div[contains(@class,"listing_title")]/a/@href').extract()

        for place in places:
            yield response.follow(place, self.parse_details)