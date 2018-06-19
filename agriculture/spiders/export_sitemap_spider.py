from scrapy.spiders import SitemapSpider

class ExportSitemapSpider(SitemapSpider):
    name = "exportssitemap"

    sitemap_urls = ['http://www.srilankabusiness.com/sitemap.xml']
    sitemap_rules = [
        ('/fruits-and-vegetables/', 'parse'),
        ('/export - agriculture/', 'parse'),
        # ('/exporters-directory/', 'parse'),
    ]
    sitemap_follow = ['/fruits-and-vegetables','/export - agriculture']
    # sitemap_follow = ['/exporters-directory']

    def parse_fruits(self, response):
        pass

    def parse_exportAgri(self, response):
        pass

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'exports-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)