# encoding=utf-8


class AutoClassify:
    """
    婴儿用品['儿','宝宝','奶瓶','母乳','玩具','乐高','泰迪熊','娃娃','公仔']
    鞋['鞋','靴','蹬']
    服装（['衣','服','裤','夹克','恤','衫','袖','外套','文胸','帽','袜','哥伦比亚']
    包['包','手袋','箱']
    电子数码['耳机','鼠标','键盘','键','音箱','音响','电脑','手机','打印机','相机','摄像机','笔记本','U盘','闪存','硬盘','存储','内存','主板']
    表、配饰['表','镜','项链','手链','戒指','腰带','手环']
    美妆香薰['剃','液','霜','膏','香水','香薰','眼线','粉底','洁面','痘','睫','护肤','凝胶','洗发','沐浴','漱口']
    营养保健['胶囊','粒','维生素','糖','鱼油','DHA','面膜','牙刷']
    生活日用['锅','厨','咖啡机','杯','壶','吸尘','拖把']
    """
    # 分十一大类
    list_on_sale = ['专场', '精选', '活动', '特卖', '金盒']
    list_baby = ['儿', '宝宝', '奶瓶', '母乳', '奶粉', 'Munchkin']
    list_toy = ['玩具', '乐高', '泰迪熊', '娃娃', '公仔', '模型', '积木', 'Nerf', '小黄人', '睿思']
    list_shoes = ['鞋', '靴', '蹬']
    list_apparel = ['衣', '服', '裤', '牛仔', '夹克', '恤', '衫', '袖', '外套',
                    '背心', '西装', '文胸', '帽', '袜', '裙', '巾', '哥伦比亚', '手套']
    list_electronics = [
        '耳机', '耳塞', '耳麦', '鼠标', '键盘', '键', '音箱', '音响', '电脑', '戴尔', '惠普',
        '手机', '打印机', '打印', '相机', '摄像机', '蓝牙', '电视', '显示器', '笔记本', 'U盘',
        '闪存', '硬盘', '存储', '内存', '主板', '充电', '屏']
    list_accessories = ['表', '镜', '项链', '手链', '戒指', '腰带', '皮带', '手环', '打火机']
    list_makeup = [
        '剃', '液', '霜', '膏', '香水', '香薰', '眼线', '粉底', '洁面', '精油', '洗脸', '痘',
        '睫', '肤', '凝胶', '洗发', '护发', '脱毛', '沐浴', '漱口', '面膜', '牙刷', '美容',
        '妆']
    list_health_food = ['胶囊', '粒', '维生素', '糖', '鱼油', 'DHA', '片', '膳食']
    list_daily = [
        '锅', '厨', '咖啡机', '杯', '壶', '桶', '罐', '吸尘', '拖把',
        '扫地', '伞', '保鲜', '烧烤', '刀', 'WMF', '帐篷', '耳温']
    list_bags = ['包', '手袋', '箱', '钱夹']

    keywords = list_on_sale + list_toy + list_baby + list_shoes + \
        list_apparel + list_electronics + list_accessories + \
        list_makeup + list_health_food + list_daily + list_bags

    def match(self, source):
        category_id = 90
        for keyword in self.keywords:
            if keyword in source:  # 在文本中匹配到关键词
                print(keyword + 'matched')
                if keyword in self.list_on_sale:
                    category_id = 92
                    break
                elif keyword in self.list_toy:
                    category_id = 93
                    break
                elif keyword in self.list_baby:
                    category_id = 76
                    break
                elif keyword in self.list_shoes:
                    category_id = 66
                    break
                elif keyword in self.list_apparel:
                    category_id = 65
                    break
                elif keyword in self.list_electronics:
                    category_id = 85
                    break
                elif keyword in self.list_accessories:
                    category_id = 67
                    break
                elif keyword in self.list_makeup:
                    category_id = 71
                    break
                elif keyword in self.list_health_food:
                    category_id = 68
                    break
                elif keyword in self.list_daily:
                    category_id = 75
                    break
                elif keyword in self.list_bags and '包邮' not in source:
                    category_id = 91
                    break
        print('category id is :' + str(category_id))
        return category_id
if __name__ == '__main__':
    source_test = '钱夹Seal Line全防水户外包芭比 35L/70L/115L可选 $69.95（约448元）起'
    autoc = AutoClassify()
    print(autoc.match(source_test))


