import scrapy
import re

def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext 

def remove_line(content) :
    cleanr = re.compile("\n")
    cleantext = re.sub(cleanr, " ", content)
    return cleantext

f=open('crawling.txt', 'w', encoding='utf-8')
class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    start_urls = ['https://music.bugs.co.kr/chart']

    def parse(self, response):
       for i in range(1,101): 

        rank_css_selector=f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(4) > div > strong"
        title_css_selector = f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > th > p > a"
        artist_css_selector = f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(8) > p > a"
        album_art_css_selector = f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(9) > a"

        rank = remove_tag(response.css(rank_css_selector).get())
        title = remove_tag(remove_line(response.css(title_css_selector).get()))
        artist = remove_tag(remove_line(response.css(artist_css_selector).get()))
        album_art = remove_tag(remove_line(response.css(album_art_css_selector).get()))

        f.write("rank : " + rank + "\n")
        f.write("title : " + title + "\n")
        f.write("artist : " + artist + "\n")
        f.write("album_art : " + album_art + "\n\n")
        
    pass
