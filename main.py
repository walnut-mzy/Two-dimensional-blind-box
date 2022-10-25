
import requests
import os
from aligo import Aligo
import cv2
import hashlib
ali = Aligo()
user = ali.get_user()
ll = ali.get_file_list()
list1=[]
# 遍历列表
checkupId = ""
filename="二次元盲盒"
for file in ll:
    # 搜索你的网盘文件夹目录
    if (file.name == filename):
        checkupId = file.file_id
        print('目录TestId:', checkupId)
def download_img(url_info):
    if url_info[1]:
        print("-----------正在下载图片 %s"%(url_info[0]))
        # 这是一个图片的url
        try:
            url = url_info[0]
            response = requests.get(url)
            # 获取的文本实际上是图片的二进制文本
            img = response.content
            # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
            #保存路径
            path="temp.png"
            with open(path, 'wb') as f:
                f.write(img)
            pic=cv2.imread(path)
            x=hashlib.md5(pic).hexdigest()
            print(x)
            print("上传完成")
            if x not in list1:
                up_file = ali.upload_file(path, checkupId)
                list1.append(x)
            else:
                print("图片重复")
                pass
            os.remove(path)
        except Exception as ex:
            print("--------出错继续----")
            print(ex)
            pass
# 第一次使用会弹出二维码，需要手机端扫描登录
for i in range(100000):
    download_img([
        "https://iw233.cn/API/Random.php"
    ])
