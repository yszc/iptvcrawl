# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#EXTM3U
#EXTINF:-1 group-title="Abroad TV",AXN
# http://50.7.61.148:30080/Entry/axn
from itemadapter import ItemAdapter


class IptvcrawlPipeline:
    def open_spider(self, spider):
        self.file = open('playlist.m3u', 'wt')
        self.file.write("#EXTM3U\n")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.writelines([
            '#EXTINF:-1 group-title="%s",%s\n' % (item['attrs'][0], item['link'][1]),
            '%s\n' % (item['link'][0])
        ])
        return item
