import scrapy


class ImportSpider(scrapy.Spider):
    name = "import_products"
    # product_category = ""
    # product_value = ""
    # product_year = ""

    start_urls = [
        'https://tradingeconomics.com/sri-lanka/imports-by-category/',
    ]

    def parse(self, response):

        for products in response.css('tr'):
            yield {

                'product_category': products.css('td a::text').extract(),
                'product_value': products.css('td::text')[2].extract().strip(),
                'product_year' : products.css('td::text')[3].extract().strip(),
            }

    # def parse(self, response):
    #     for url in response.css('tr'):
    #         self.product_category: url.css('td a::text').extract()
    #         self.product_value: url.css('td::text')[2].extract().strip()
    #         self.product_year: url.css('td::text')[2].extract().strip()
    #
    #         next_link = url.css('td a::attr(href)').extract_first()
    #         new_url = response.urljoin(next_link)
    #         yield scrapy.Request(new_url, self.imports)
