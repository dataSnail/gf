# -*- coding: utf-8 -*- 

# author:mq

import time
import math
import random
import logging
import numpy as np
import pandas as pd
from tqdm import tqdm
from collections import defaultdict


logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)

from dc_parser import parameter_parser

dd = defaultdict(int)
LAYER = 2

def countDistance(node_id,length,adjacency):
    global dd
    global LAYER
    # print(length)
    neighbors = adjacency[int(node_id)].strip('\n').split('\t')
    if length <=0 or len(neighbors)<=4:
        dd[node_id] = dd[node_id]+math.pow(1/2,LAYER-1-length) #accumulating weight for leaves
        return math.pow(1/2,LAYER-2-length)
    for i in range(int(len(neighbors[4:])/2)):
        cc = countDistance(neighbors[4+2*i],length-1,adjacency)
        dd[node_id] = dd[node_id]+cc
    return (len(neighbors[4:])/2)*math.pow(1/2,LAYER-2-length)

# def countDistance_friendsPreference(node_id,length):
#     neighbors = adjacency[int(node_id)].strip('\n').split('\t')
#     if length <=0 or len(neighbors)<=4:
#     #         if LAYER == length:
#     #             dd[node_id] = dd[node_id]+math.pow(1/2,LAYER-length) 
#         dd[node_id] = dd[node_id]+math.pow(1/2,LAYER-1-length) #accumulating weight for leaves
#         return math.pow(1/2,LAYER-2-length)
#     for i in range(int(len(neighbors[4:])/2)):
#         cc = countDistance_friendsPreference(neighbors[4+2*i],length-1)
#         dd[node_id] = dd[node_id]+cc
#     return (len(neighbors[4:])/2)*math.pow(1/2,LAYER-2-length)


def thread_worker_path(start_uid,end_id,thread_id,adjacency):
    logging.info('Thread worker id:%s, start uid:%s, end_id:%s'%(thread_id,start_uid,end_id-1))
    global dd
    global LAYER
    if end_id>18789:
        end_id=18789
    with open('./data/mid_percetion_%s_start_%s_end_%s.txt'%(thread_id,start_uid,end_id),'a') as data_file:
        for i in tqdm(range(start_uid,end_id)):
            dd.clear()
            countDistance(i,LAYER,adjacency)
            dd_df = pd.DataFrame.from_dict(dd,orient='index')#.sort_values(by=0,ascending=False)
            data_file.write((pd.DataFrame.to_string(dd_df.sort_values(by=0,ascending=False)[:500],header=False)).replace('\n',';'))
            data_file.write('\n')
            del dd_df

def main(args):
    start_time = time.time()
    with open('./data/mid_network_friends.txt') as net_f:
        adjacency = net_f.readlines()
    print('loading files end!')
    thread_worker_path(args.start_id,args.end_id,args.worker_id,adjacency)

    end_time = time.time()
    print('End...\nThe program is running for %.2f seconds'%(end_time-start_time))

if __name__ == '__main__':
    args = parameter_parser()
    main(args)