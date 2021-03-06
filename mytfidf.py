#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : keywords_tfidf.py
# Create date : 2019-08-19 11:52
# Modified date : 2020-05-23 16:29
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import jieba.posseg as pseg
import os

class TFIDF:
    def __init__(self):
        cur = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.idf_file_path = os.path.join(cur, 'data/idf.txt')
        self.idf_dict, self.avg_idf = self.load_idf_dict(self.idf_file_path)

    def build_tf_dict(self, text):
        word_dict = {}
        candi_words = []
        drop_words = []
        for word in pseg.cut(text):
            if word.flag[0] in ['n', 'v', 'a'] and len(word.word) > 1:
                candi_words.append(word.word)
            word_dict[word.word] = word_dict.get(word.word, 0) + 1

        count_total = sum(word_dict.values())
        candi_dict = {word: word_dict[word]/count_total for word in candi_words}
        return candi_dict

    def extract_keywords(self, text, num_keywords):
        keywords_dict = {}
        tf_dict = self.build_tf_dict(text)
        tfidf_dict = {w:self.idf_dict.get(w, self.avg_idf)*tf_dict[w] for w in tf_dict}
        keywords_dict = sorted(tfidf_dict.items(), key=lambda asd:asd[1], reverse=True)
        return keywords_dict[:num_keywords]

    def load_idf_dict(self, idf_file_path):
        idf_dict = {}
        
        for line in open(idf_file_path):
            word, freq = line.strip().split(' ')
            idf_dict[word] = float(freq)

        avg_idf = sum(idf_dict.values())/len(idf_dict)

        return idf_dict, avg_idf

def test():
    text = '''（原标题：央视独家采访：陕西榆林产妇坠楼事件在场人员还原事情经过）
    央视新闻客户端11月24日消息，2017年8月31日晚，在陕西省榆林市第一医院绥德院区，产妇马茸茸在待产时，从医院五楼坠亡。事发后，医院方面表示，由于家属多次拒绝剖宫产，最终导致产妇难忍疼痛跳楼。但是产妇家属却声称，曾向医生多次提出剖宫产被拒绝。
    事情经过究竟如何，曾引起舆论纷纷，而随着时间的推移，更多的反思也留给了我们，只有解决了这起事件中暴露出的一些问题，比如患者的医疗选择权，人们对剖宫产和顺产的认识问题等，这样的悲剧才不会再次发生。央视记者找到了等待产妇的家属，主治医生，病区主任，以及当时的两位助产师，一位实习医生，希望通过他们的讲述，更准确地还原事情经过。
    产妇待产时坠亡，事件有何疑点。公安机关经过调查，排除他杀可能，初步认定马茸茸为跳楼自杀身亡。马茸茸为何会在医院待产期间跳楼身亡，这让所有人的目光都聚焦到了榆林第一医院，这家在当地人心目中数一数二的大医院。
    就这起事件来说，如何保障患者和家属的知情权，如何让患者和医生能够多一份实质化的沟通？这就需要与之相关的法律法规更加的细化、人性化并且充满温度。用这种温度来消除孕妇对未知的恐惧，来保障医患双方的权益，迎接新生儿平安健康地来到这个世界。'''
    tfidfer = TFIDF()
    for keyword in tfidfer.extract_keywords(text, 10):
        print(keyword)

    '''
     ('产妇', 0.16089872363839283)
     ('医院', 0.10469306102267856)
     ('待产', 0.10192652680535713)
     ('剖宫产', 0.09611770924999999)
     ('家属', 0.09150082801845238)
     ('坠亡', 0.069497286319104)
     ('事件', 0.06781284802178572)
     ('跳楼', 0.061929583872023804)
     ('患者', 0.056677817569285714)
     ('榆林', 0.053159906859523806)
    '''

if __name__ == '__main__':
    test()
