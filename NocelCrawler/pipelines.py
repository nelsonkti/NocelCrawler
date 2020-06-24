# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class NocelcrawlerPipeline(object):
    # __init__函数里面初始化就是连接数据库，便于实现增删改查
    def __init__(self):
        # connection database
        self.connect = pymysql.connect('localhost', 'root', '123456', 'test')  # 后面三个依次是数据库连接名、数据库密码、数据库名称
        # get cursor
        self.cursor = self.connect.cursor()
        print("连接数据库成功")

    def process_item(self, item, spider):
        print("开始输入数据")
        try:

            self.cursor.execute(
                "insert into novel(title, context,url) values (%s, %s, %s)",
                (item['title'], item['context'], item['url']))
            self.connect.commit()
        except Exception as error:
            # print error
            print(error)
        return item
