#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description'
__author__ = '13314409603@163.com'
import os

#windows
base_dir = 'E:\\pyWorkspace\\myBert'
#linux
# base_dir ='/home/myBert'

event_type='结婚'

data_dir=os.path.join(base_dir,'BERT-EVENT')
bert_model_dir = os.path.join(base_dir,'chinese_L-12_H-768_A-12')
task_name='event'
vocab_file=os.path.join(bert_model_dir,'bert_config.json')
output_dir = os.path.join(base_dir,'out_put2')
bert_config_file=os.path.join(bert_model_dir,'bert_config.json')
init_checkpoint=os.path.join(bert_model_dir,'bert_model.ckpt')
init_checkpoint=os.path.join(output_dir,'bert_model.ckpt')
do_train=True
do_dev=False
do_predict = True
event_seed_size = 100

#mask标记
MASK = '*'

#tigger window size
MASK_MAX_LENGTH=4

#mask之后，如果event seed list里超过triiger_threshold的event不为true，则说明mask的词为trigger
trigger_threshold = 0.7

if __name__ == '__main__':
    pass