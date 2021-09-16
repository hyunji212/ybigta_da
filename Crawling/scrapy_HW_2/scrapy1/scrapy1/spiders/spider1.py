import scrapy
import re

def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext

def get_id(content):
    url=content.split('track/')[1].split('?')[0]
    return url

f = open("urls.txt", 'w', encoding='utf-8')    
class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    start_urls = ['https://music.bugs.co.kr/chart']

    def parse(self, response):
        for i in range(1,101):
            url_format="https://music.bugs.co.kr/track/"
            url_f = "?wl_ref=list_tr_08_chart"
            css_selector=f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(6) > a"
            page_id=get_id(response.css(css_selector).get())
            url=url_format + page_id + url_f
            f.write(url + "\n")
        pass