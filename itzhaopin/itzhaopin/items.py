# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class TencentItem(Item):
    name = Field()
    catalog = Field()
    workLocation = Field()
    recruitNumber = Field()
    detailLink = Field()
    publishTime = Field()

