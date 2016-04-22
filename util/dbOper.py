#!/usr/bin/env python
# coding=utf8

import MySQLdb    


class DBOperator:
    
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='root', charset='utf8')  # 'gbk'
        self.conn.select_db('haitaocn')

    def insert_product(self, value):
        cursor = self.conn.cursor()
        cursor.execute("insert into mcc_product(model,isbn,image) values(%s,%s,%s)", value)
        cursor.close()
        self.conn.commit()

    def get_product_id(self, value):
        cursor = self.conn.cursor()
        cursor.execute("SELECT product_id FROM mcc_product WHERE model = %s", value)
        product_id = cursor.fetchall()
        cursor.close()
        return product_id
             
    def insert_product_des(self, value):
        cursor = self.conn.cursor()
        cursor.execute("insert into mcc_product_description(product_id,name,description,meta_title) values(%s,%s,%s,%s)", value)
        cursor.close()
        self.conn.commit()

    def insert_category(self, value):
        cursor = self.conn.cursor()
        cursor.execute("insert into mcc_product_to_category (product_id,category_id) values (%s,%s)",value)
        cursor.close()
        self.conn.commit()    
        
    def insert_to_store(self, value):
        cursor = self.conn.cursor()
        cursor.execute("insert into mcc_product_to_store (product_id) values (%s)", value)
        cursor.close()
        self.conn.commit()

    def insert_alias(self, value):
        cursor = self.conn.cursor()
        cursor.execute("insert into mcc_url_alias (query,keyword) values (%s,%s)",value)
        cursor.close()
        self.conn.commit()
        
    def close_db(self):
        self.conn.close()
