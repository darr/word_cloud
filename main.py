#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-19 12:24
# Modified date : 2019-08-19 14:15
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from create_cloud import CreateWordCloud

def test_content():
    picturefile = 'jiangxi.jpeg'
    content = '''
 江西之美
豫章故郡，洪都新府,星分翼轸，地接衡庐。襟三江而带五湖，控蛮荆而引瓯越。物华天宝，龙光射牛斗之墟；人杰地灵，徐孺下陈蕃之榻。雄州雾列，俊采星驰……。这是唐代著名诗人王勃《藤王阁序》中介绍江西首府“南昌”的诗，江西的情况从这儿可以略知一二，南昌还有世界动感都会、文明花园城市之称，更是中国人民解放军的诞生地，有英雄城之称。
江西，简称赣，是典型的江南鱼米之乡。因公元733年唐玄宗设江南西道而得省名。是人杰地灵、钟灵毓秀、物华天宝之处。江西是革命老区，江西人民为中国革命做出了卓著贡献，毛主席等老一辈无产阶级革命家创建的第一个革命根据地“井冈山”就在江西，经过解放后改革开放几十年的发展，江西成为中国经济比较发达的内陆对外开放省份。江西东邻浙江、福建，南嵌广东，西靠湖南，北毗湖北、安徽而共接长江，为长江三角洲、珠江三角洲和闽南三角洲经济发达地区的共同腹地，区位极为优越。省境内除北部较为平坦外，东西南部三面环山，中部丘陵起伏，成为一个整体向鄱阳湖倾斜而往北开口巨大盆地。全境有大小河流2400余条，赣江、抚河、信江、修河和饶河为江西五大河流，江西的风景形胜也是全国独特，李白的《望庐山瀑布》一诗描写了庐山的壮美，其实江西的三清山、龙虎山等与庐山是难分伯仲的，三清山是世界文化自然遗产，您只要上一回三清山，就感到它不亚于黄山，真是仙人之居所。不亏为世界第一的花岗岩山……大美的江西，人间的天堂
    '''
    save_name = 'jiangxi'
    words_num = 50
    handler = CreateWordCloud()
    #handler.show_wordcloud_input(content, picturefile, words_num, save_name)
    handler.show_wordcloud_input(content, None, words_num, save_name)

def test_url():
    picturefile = 'huawei.jpeg'
    url = 'https://news.sina.com.cn/o/2019-01-26/doc-ihrfqzka1140567.shtml'
    save_name = 'huawei'
    words_num = 50
    handler = CreateWordCloud()
    handler.show_wordcloud_online(url, picturefile, words_num, save_name)
    #handler.show_wordcloud_online(url, None, words_num, save_name)

def test_local_text():
    picturefile = 'mao.jpg'
    textfile = 'mao.txt'
    save_name = 'mao'
    words_num = 50
    handler = CreateWordCloud()
    handler.show_wordcloud_offline(textfile, picturefile, words_num, save_name)
    #handler.show_wordcloud_offline(textfile, None, words_num, save_name)

def run():
    test_content()
    test_url()
    test_local_text()
    print("生成云图在./output/文件夹中")

run()
