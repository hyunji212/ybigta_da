import scrapy
import re
def remove_tag(content):
    cleanr =re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext


def remove_artist(content):
    cleanr =re.compile('CONNECT 아티스트')
    cleantext = re.sub(cleanr, '', content)
    return cleantext

def remove_line(content):
    cleanr =re.compile('\n')
    cleantext = re.sub(cleanr, '', content)
    return cleantext

f = open("description.txt", 'w', encoding='utf-8')

class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    start_urls = ['']

    def start_requests(self):
        with open("C:/Users/Jeong Hyunji/Desktop/학회/DA TEAM/Crawling/scrapy_HW_2/scrapy1/urls.txt", "r") as f:
            while True:
                url = f.readline()
                print(url)
                if not url:
                    break
                yield scrapy.Request(url=url, callback=self.get_detail)

    def get_detail(self, response):

       title = remove_tag(response.css("#container > header > div > h1").get()).strip()
       f.write("Title : "+ title + "\n")
       artist=remove_tag(remove_artist(response.css("#container > section.sectionPadding.summaryInfo.summaryTrack > div > div.basicInfo > table > tbody > tr:nth-child(1) > td > a").get())).strip()
       f.write("Artist : "+ artist + "\n")
       album= remove_tag(response.css("#container > section.sectionPadding.summaryInfo.summaryTrack > div > div.basicInfo > table > tbody > tr:nth-child(3) > td > a").get())
       f.write("Album : "+ album + "\n")
       time=remove_tag(response.css("#container > section.sectionPadding.summaryInfo.summaryTrack > div > div.basicInfo > table > tbody > tr:nth-child(4) > td > time").get())
       f.write("Time : "+ time +"\n")
       lyrics=remove_tag(remove_line(response.css("#container > section.sectionPadding.contents.lyrics > div > div > xmp").get()))
       f.write("<Lyrics>"+  "\n")
       f.write(lyrics +"\n\n")