import scrapy


class GeekHackSpider(scrapy.Spider):
    name = "geekhack"

    def start_requests(self):
        urls = [
            "https://geekhack.org/index.php?board=132.0"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # response.xpath("//td[@class='subject windowbg2']/div/span/a/text()").getall()
        # response.xpath("//a[@class='navPages']/text()").getall()