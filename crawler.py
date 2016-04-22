# -*- coding: utf-8 -*-
import re
import urllib
import time
import requests
import codecs
from bs4 import BeautifulSoup


class Crawler:
    """
    crawl and pre_process data from guangdiu website。
    """

    @staticmethod
    def process_description(origin_description):
        replace_words = {'值友', '分友'}
        delete_words = {'一分', '点击购买>>', '点击加入', '点击', '立即购买>>', '惠惠一键', '惠惠', '\t'}
        new_description = origin_description

        for word in replace_words:
            pattern = re.compile(word)
            new_description = re.sub(pattern, '网友', new_description)
        for word in delete_words:
            new_description = new_description.replace(word, '')
        print(new_description)
        return new_description

    def get_product_description(self, detail_url):
        """
        Return detail description of product
        """
        response = urllib.request.urlopen(detail_url)
        web_data = response.read()
        soup = BeautifulSoup(web_data, 'lxml')
        descriptions_list = soup.select('#dabstract > p')
        for item in soup.select('#dabstract > div > p'):
            descriptions_list.append(item )
        description = ''
        for description_tag in descriptions_list:
            description += description_tag.get_text().strip()
        new_description = self.process_description(description)
        return new_description

    def get_product_info(self, pages=30):
        """
        :param pages: how many pages to crawl
        :return: img_link,save_path,img_name,title,asin
        """
        pattern1 = re.compile('http://(.*).jpg')
        pattern2 = re.compile("((?!/).)*\.jpg")
        pattern3 = re.compile("(?!/)B[a-zA-Z0-9]{9}")
        turn_pages_list = [
            'http://guangdiu.com/cate.php?p={page}&m=Amazon&c=us'
            .format(page=i) for i in range(1, pages+1)]
        response = urllib.request.urlopen(turn_pages_list[0])
        web_data = response.read()
        soup = BeautifulSoup(web_data, 'lxml')
        img_links = soup.select('#mainleft > div.zkcontent > div > div.imgandbtn > div.showpic > a > img')
        titles = soup.select("#mainleft > div.zkcontent > div > div.iteminfoarea > h2 > a.goodname")
        asins = soup.select("#mainleft > div.zkcontent > div > div.rightlinks > a")
        all_info = ['image URL  image_Save_Path  image_Name  title  description  asin']
        for img_link_tag, title_tag, asin_tag in zip(img_links, titles, asins):
            img_link = pattern1.match(img_link_tag.get('src').strip()).group()
            img_name = pattern2.search(img_link).group()
            save_path = 'catalog/' + img_name
            title = title_tag.get_text().strip()
            detail_url = 'http://guangdiu.com/' + title_tag.get('href')
            description = self.get_product_description(detail_url)
            time.sleep(2)
            asin = pattern3.search(asin_tag.get('href'))
            if asin:
                asin = asin.group()
            else:
                asin = ' '
            all_info.append(img_link + '\t' + save_path + '\t' + img_name +
                            '\t' + title + '\t' + description + '\t' + asin)
        with codecs.open('./guangdiu.txt', 'w+', 'utf-8') as f:
            f.writelines(x + '\r\n' for x in all_info)
if __name__ == '__main__':
    crawler = Crawler()
    crawler.get_product_info()
    # Crawler.process_description("中文字符串值友分友是什么点击购买>>代立即购买课老师")
