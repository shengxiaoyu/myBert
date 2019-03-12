#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

__doc__ = 'description'
__author__ = '13314409603@163.com'
from bert_base.bert.run_classifier import EventProcesss
import os

MASK = '*'
MASK_MAX_LENGTH=4
#构造mask之后的数据，给模型predict
def formTestData(savePath):
    maskPath = os.path.join(savePath,'mask')
    with open(os.path.join(savePath,'train_event.txt'),'r',encoding='utf8') as f:
        eventLines = f.readlines()#event seed list
        for index in range(len(eventLines)):
            if(index>=10): #全部做完太大，暂时只做1000个
                break
            #新建文件夹，每个文件夹对应一个mask的原句子
            basePath = os.path.join(maskPath,str(index+1))
            os.mkdir(basePath)
            #mask and mased sentence
            tasks,taskedSentences = maskSentence(eventLines[index],MASK_MAX_LENGTH)

            #form data to predict
            newIndex = 1
            for mask,maskedSentence in zip(tasks,taskedSentences):
                #每个文件对应一个mask方式-其余所有的event seed list
                with open(os.path.join(basePath, str(newIndex) + '.txt'), 'w', encoding='utf8') as fw:
                    for otherIndex in range(len(eventLines)):
                        if(otherIndex!=index):
                            fw.write('\t'.join([mask,maskedSentence,eventLines[otherIndex]]))
                newIndex += 1

def maskSentence(sentence,mask_max_length):
    sentence = sentence.strip()
    sentenceLength = len(sentence)
    masks = []
    maskedSentence = []
    for i in range(0,sentenceLength):
        for j in range(1,mask_max_length+1):
            if(i+j<=sentenceLength):
                masked = sentence[i:i+j]
                newSentence = ''.join(sentence[0:i])+''.join(['*' for _ in range(j)])+''.join(sentence[i+j:-1])
                masks.append(masked)
                maskedSentence.append(newSentence)
            else:
                break
    return masks,maskedSentence

if __name__ == '__main__':
    formTestData('C:\\Users\\13314\\Desktop\\BERT-EVENT')
    sys.exit(0)
    # pass