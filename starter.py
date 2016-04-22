import os
import time
from util.autoClassify import AutoClassify
from util.imageLoader import ImageLoader
from util.dbOper import *


class Starter:

    @staticmethod
    def open_get_ata(self, file):
        # 下载图片、操作数据库类及自动分类的实例化
        imagel = ImageLoader()
        db_o = DBOperator()
        ac_o = AutoClassify()
        # 打开原始数据文件及去重（依据图片名）文件
        f1 = open(file, 'r')
        f2 = open('imageNameList.txt', 'a+')
        # 打开modelList.txt获取上次执行后的最后一个model
        f3 = open('model.txt', 'a+')
        try:
            li3 = f3.readlines()
            model = int(li3[-1])
            print('start from model NO.: ' + str(model))
        except Exception as e:
            print("[Error]Can't read lastModel.txt : %s" % e)
        # 开始提取字段
        try:
            li1 = f1.readlines()[1:]    # [1,n]意思是从第二行开始，一共读出（N-1）行。
            li2 = f2.readlines()[0:]    # 打开用来保存图片名的txt文档，用以判断此图片（产品）是否已经添加过。

            for line_f1 in reversed(li1):   # 倒序从原始数据文档中读取，以保证最新添加的商品出现在（首页-最新商品）的第一个
                line_f1 = line_f1.strip()
                line_f1 = line_f1.split('\t')
                if len(line_f1) < 5:
                    continue
                if len(line_f1) == 5:    # 如果第一个或者最后一个字段未抓到，会报错下面的list索引超出范围。asin比较可能抓不到，就给个空字符串。可以给下面的数据库操作加try，暂未成功
                    line_f1.append('')

                line_f1[3] = line_f1[3].strip()  # 默认删除空白符（包括'\n', '\r',  '\t',  ' ')
                line_f1[4] = line_f1[4].strip()

                if(line_f1[2] + '\n') in li2:
                    continue
                else:    # 如果判断txt中无此图片记录，添加此新的文件名并返回原始字段以插入数据库
                    f2.writelines(line_f1[2] + '\n')
                    print('Add imageNameList record')
                    model += 1
                    f3.write(str(model) + '\n')
                    print('add model record')
                    # 下载图片
                    imagel.get_save_img(line_f1[0], line_f1[2])
                    time.sleep(2)
                    print('download image：' + line_f1[2])
                    self.operate_db(db_o, ac_o, model, line_f1)
            print('end with model NO.: ' + str(model))
        finally:
            f1.close()
            f2.close()
            f3.close()
            db_o.close_db()

    @staticmethod
    def operate_db(self, dbo, ac , model, line_f):

        # 以下为数据库操作,插入到product表
        product = [str(model), line_f[5], line_f[1]]  # 参数插入表中 model asin image 三个字段
        dbo.insert_product(product)
        # 获取自动生成产品id，并插入产品描述表
        product_id = dbo.get_product_id(model)[0][0]
        print('product id :' + str(product_id))
        product_description = [product_id, line_f[3], line_f[4], line_f[3]]  # name,description,meta_title
        dbo.insert_product_des(product_description)
        # 将自动识别的分类id和对应产品id插入分类表
        print(line_f[3])
        category_id = ac.match(line_f[3])
        category = [product_id, category_id]
        dbo.insert_category(category)
        # 将自动生成的产品id插入商城表
        dbo.insert_to_store(product_id)
        # 插入seo alias
        query = 'product_id=' + str(product_id)
        alias = [query, str(model) + '.html']
        dbo.insert_alias(alias)

if __name__ == '__main__':
    file_name = 'guangdiu.txt'
    fr = Starter()
    fr.open_get_ata(file_name)
    os.system("pause")

