#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import math

__doc__ = 'description'
__author__ = '13314409603@163.com'

MAX_LENGTH = 1000
LENGTHS = [0 for _ in range(MAX_LENGTH)]
SUMS = [0 for _ in range(MAX_LENGTH)]
COUNT = 1
#统计句子长度分布
def calSentenceLength(path):
    if(os.path.isdir(path)):
        for subPath in os.listdir(path):
            calSentenceLength(os.path.join(path,subPath))
    else:#统计单个文件
        with open(path, 'r', encoding='utf8') as f:
            for sentence in f.readlines():
                length = len(sentence.strip())
                LENGTHS[length] += 1

#输入占比区间，例如输入0.95，返回包含95%的句子此时需要设置句子长度的阈值
def getMax(rate):
    sum = 0
    for index,count in enumerate(LENGTHS):
        sum += count
        SUMS[index] = sum
    for index in range(MAX_LENGTH):
        if(SUMS[index]/SUMS[-1]>=rate):
            return index

#计算句子平均长度
def getMean():
    totalLength = 0
    sum = 0
    for index,value in enumerate(LENGTHS):
        totalLength += index*value
        sum += value
    print(totalLength/sum)

#将案号转为indxe 文件名称
def an2Index(path):
    if(not os.path.exists(path)):
        return
    elif(os.path.isdir(path)):
        for file in os.listdir(path):
            an2Index(os.path.join(path,file))
    else:
        global COUNT
        os.renames(path,os.path.join(os.path.dirname(path),str(COUNT)+'.txt'))
        COUNT += 1
import math
#将一个文件夹下的文件列表分割转入子文件夹
def divideFile(savePath,cap):
    fileNames = os.listdir(savePath)
    num = math.ceil(float(len(fileNames))/cap)
    for i in range(num):
        newDir = os.path.join(savePath,str(i+1))
        os.mkdir(newDir)
        beginIndex = i*cap
        endIndex = (i+1)*cap
        endIndex = endIndex if endIndex<len(fileNames) else -1
        for fileName in fileNames[beginIndex:endIndex]:
            os.rename(os.path.join(savePath,fileName),os.path.join(newDir,fileName))
def rename(path):
    for dir in os.listdir(path):
        baseDir = os.path.join(path, dir)
        for fileName in os.listdir(baseDir):
            os.rename(os.path.join(baseDir, fileName), os.path.join(baseDir, fileName.replace('.xml', '.txt')))


if __name__ == '__main__':
    # calSentenceLength('C:\\Users\\13314\\Desktop\\BERT-EVENT\\train_event.txt')
    # with open('C:\\Users\\13314\\Desktop\\BERT-EVENT\\sentence-length.txt','w',encoding='utf8') as fw:
    #     fw.write('\n'.join(map(lambda x:str(x),LENGTHS)))
    # getMean()
    # divideFile('C:\\Users\\13314\\Desktop\\Bi-LSTM+CRF\\segment_result\\cpws',100)
    rename('C:\\Users\\13314\\Desktop\\Bi-LSTM+CRF\\segment_result\\cpws')
    sys.exit(0)