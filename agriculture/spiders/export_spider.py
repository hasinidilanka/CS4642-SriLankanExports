import scrapy


class ExportSpider(scrapy.Spider):
    name = "export_products"
    title = ""

    start_urls = [
        'http://www.srilankabusiness.com/exporters-directory/',
    ]

    def exports(self, response):

        for products in response.css('div.search-row'):
            yield {
                'main_title': self.title,
                'company_name': products.css('a::attr(title)').extract_first(),
                'company_url': products.css('a::attr(href)').extract_first(),
                'company_logo': products.css('a img::attr(src)').extract(),
                'product_range': products.css('div.products div.nitinh-vAlign p::text').extract(),
                'product_category': products.css('div.more.columns p::text').extract(),
            }

    def parse(self, response):
        for url in response.css('div.content-wrapper ul li'):
            self.title = url.css('a::attr(title)').extract_first()
            next_link = url.css('a::attr(href)').extract_first()
            new_url = response.urljoin(next_link)
            yield scrapy.Request(new_url, self.exports)




