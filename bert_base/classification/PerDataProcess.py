#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description'
__author__ = '13314409603@163.com'
import os
import random
import sys
Key = '结婚'

#抽取结婚句子和噪音句子
def extractionEventSentence(basePath):
    eventSentences = os.path.join(basePath,'event.txt')
    noiseSentences = os.path.join(basePath,'noise.txt')
    source_data_path = os.path.join(basePath,'source_data')
    with open(eventSentences,'w',encoding='utf8') as eventfw,open(noiseSentences,'w',encoding='utf8') as noisefw:
        for fileName in os.listdir(source_data_path):
            with open(os.path.join(source_data_path,fileName),'r',encoding='utf8') as f:
                #结婚事件只找前两行
                eventLine = f.readline() ;
                if(eventLine.find(Key)==-1):
                    eventLine = f.readline()
                if(eventLine!=None and eventLine.find(Key)!=-1):

                    #去掉诉称
                    index = eventLine.find('诉称')
                    if(index==-1):
                        eventLine = eventLine[index + 3:-1]
                    else:
                        index = eventLine.find('称')
                        if(index!=-1):
                            eventLine = eventLine[index + 2:-1]
                    #为确保换行，手动添加\n
                    eventfw.write(eventLine.strip())
                    eventfw.write('\n')

                    noiseLines= f.readlines()
                    if(noiseLines!=None and len(noiseLines)>0):#添加随机剩余的两行作为noist,但这两行要排除被告辩称含“结婚”的字
                        if(len(noiseLines)==1):
                            if(noiseLines[0].find(Key)!=-1):
                                continue
                            noisefw.write(noiseLines[0].strip())
                            noisefw.write('\n')
                        elif(len(noiseLines)==2):
                            if(noiseLines[0].find('辩称')==-1):
                                noisefw.write(noiseLines[0].strip())
                                noisefw.write('\n')
                            if(noiseLines[1].find('辩称')==-1):
                                noisefw.write(noiseLines[1].strip())
                                noisefw.write('\n')
                        else:
                            #随机添加两行，要排除被告辩称含结婚的情况
                            noiseLine = noiseLines[random.randint(0, len(noiseLines) - 1)].strip()
                            while(noiseLine.find('辩称')!=-1):
                                noiseLine = noiseLines[random.randint(0, len(noiseLines) - 1)].strip()
                            noisefw.write(noiseLine)
                            noisefw.write('\n')

                            noiseLine = noiseLines[random.randint(0, len(noiseLines) - 1)].strip()
                            while (noiseLine.find('辩称') != -1):
                                noiseLine = noiseLines[random.randint(0, len(noiseLines) - 1)].strip()
                            noisefw.write(noiseLine)
                            noisefw.write('\n')

#分割结婚句子和噪音句子为训练、评估、测试三份
def splitTrainDevTest(savePath):
    eventPath = os.path.join(savePath,'event.txt')
    noisePath = os.path.join(savePath,'noise.txt')

    train_event_path = os.path.join(savePath,'train_event.txt')
    train_noise_path = os.path.join(savePath,'train_noise.txt')

    dev_event_path = os.path.join(savePath,'dev_event.txt')
    dev_noise_path = os.path.join(savePath,'dev_noise.txt')

    test_event_path = os.path.join(savePath,'test_event.txt')
    test_noise_path = os.path.join(savePath,'test_noise.txt')
    with open(eventPath,'r',encoding='utf8') as f,open(train_event_path,'w',encoding='utf8') as trainfw,open(dev_event_path,'w',encoding='utf8') as devfw,open(test_event_path,'w',encoding='utf8')as testfw:
        eventSentences = f.readlines()
        testfw.writelines(eventSentences[0:2184])
        devfw.writelines(eventSentences[2184:7184])
        trainfw.writelines(eventSentences[7184:-1])
    with open(noisePath,'r',encoding='utf8') as f,open(train_noise_path,'w',encoding='utf8') as trainfw,open(dev_noise_path,'w',encoding='utf8') as devfw,open(test_noise_path,'w',encoding='utf8')as testfw:
        noiseSentences = f.readlines()
        testfw.writelines(noiseSentences[0:3056])
        devfw.writelines(noiseSentences[3056:13056])
        trainfw.writelines(noiseSentences[13056:-1])
if __name__ == '__main__':
    basePath = 'C:\\Users\\13314\\Desktop\\BERT-EVENT'
    extractionEventSentence(basePath)
    splitTrainDevTest(basePath)
    # print(random.randint(0,4))
    sys.exit(0)

