# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import json
import codecs

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('logo.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class DownloadImagesPipeline(ImagesPipeline):
    def get_media_requests(self,item,info): #����ͼƬ
        for image_url in item['imageurl']:
            yield Request(image_url,meta={'item':item,'index':item['imageurl'].index(image_url)}) #���meta��Ϊ�������������ļ���ʹ��

    def file_path(self,request,response=None,info=None):
        item=request.meta['item'] #ͨ�������meta���ݹ���item
        index=request.meta['index'] #ͨ�������index���ݹ����б��е�ǰ����ͼƬ���±�

        #ͼƬ�ļ�����item['carname'][index]�õ��������ƣ�request.url.split('/')[-1].split('.')[-1]�õ�ͼƬ��׺jpg,png
        image_guid = item['carname'][index]+'.'+request.url.split('/')[-1].split('.')[-1]
        #ͼƬ����Ŀ¼ �˴�item['country']����Ҫǰ��item['country']=''.join()......,����Ŀ¼������\u97e9\u56fd\u6c7d\u8f66\u6807\u5fd7\xxx.jpg
        filename = u'full/{0}/{1}'.format(item['country'], image_guid) 
        return filename
