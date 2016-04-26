# -*- coding: UTF-8 -*-
import urllib
import socket


class ImageLoader:

    @staticmethod
    def get_save_img(image_url, image_name):
        timeout = 10
        local_path = 'C:\phpStudy\WWW\Haitaocn\image\catalog' + '\\' + image_name
        try:  # 不论是否捕获异常都会执行
            urllib.urlretrieve(image_url, local_path)
            socket.setdefaulttimeout(timeout)
        except Exception as e:
            print("[Error]Cant't download_weheartit: %s:%s" % (local_path, e))
