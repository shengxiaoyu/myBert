#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

__doc__ = 'description'
__author__ = '13314409603@163.com'
from bert_base import config
import os


#构造mask之后的数据，给模型predict
def formMaskData(savePath):
    maskPath = os.path.join(savePath,'mask')
    with open(os.path.join(savePath,'train_event.txt'),'r',encoding='utf8') as f:
        eventLines = f.readlines()#event seed list
        for index in range(len(eventLines)):
            if(index>=config.event_seed_size): #全部做完太大，暂时只做1000个
                break
            #新建文件夹，每个文件夹对应一个mask的原句子
            basePath = os.path.join(maskPath,str(index+1))
            os.mkdir(basePath)
            #mask and mased sentence
            tasks,taskedSentences = maskSentence(eventLines[index],config.MASK_MAX_LENGTH)

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
                newSentence = ''.join(sentence[0:i])+''.join([config.MASK for _ in range(j)])+''.join(sentence[i+j:-1])
                masks.append(masked)
                maskedSentence.append(newSentence)
            else:
                break
    return masks,maskedSentence

def getTrigger():
    with open(os.path.join(config.data_dir,'test_results1.tsv'),'r',encoding='utf8') as resultReader:
        results = resultReader.readlines()
    basePath = os.path.join(config.data_dir,'mask')
    beginIndex =0

    with open(os.path.join(basePath,'trigger.txt'),'w',encoding='utf8') as fw:
        for dirName in os.listdir(basePath):
            #每个mask原句子中产生的trigger数
            triggers = []
            dirPath = os.path.join(basePath,dirName)
            for fileName in os.listdir(dirPath):
                with open(os.path.join(os.path.join(dirPath,fileName)),'r',encoding='utf8') as fr:
                    lines = fr.readlines()
                    maskWord = lines[0].split('\t')[0]
                    count = 0
                    for result in results[beginIndex:len(lines)]:
                        if(result=='False'):
                            count += 1
                    prec = count/len(lines)
                    if(prec>=config.trigger_threshold):
                        triggers.append(maskWord)

        fw.write(','.join(triggers))
        fw.write('\n')

def formPredictData(sentence,fileName):
    testDir = os.path.join(config.data_dir,'test')
    with open(os.path.join(testDir,fileName),'w',encoding='utf8') as fw:
        count = 0
        with open(os.path.join(config.data_dir,'dev_event.txt'),'r',encoding='utf8') as f:
            while(count<config.event_seed_size):
                fw.write(sentence+'\t'+f.readline().strip()+"\n")
                count += 1

if __name__ == '__main__':
    sys.exit(0)
    # pass