# -*- coding: utf-8 -*- 

# author:mq

import logging
import numpy as np
import time
from tqdm import tqdm
from dc_parser import parameter_parser

# '''
# clean data using form 'uid\tneighbors_num\tfriends_num\tnofriends_num\tfid\tfriend_flag ...
# '''
logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)

def dealData(from_file_name,to_file_name):
    lines = None
    with open(from_file_name,'r') as net_rf:
        lines = net_rf.readlines()

    logging.info('read file %s end.'%from_file_name)

    with open(to_file_name,'w') as net_wf:
        for i in tqdm(range(len(lines))):
            temp = lines[i].strip('\n').strip('\t').split('\t')
            # total = int(temp[0:1][0]) #the total number of neighbors
            friends = []
            nofriends = []
            j = 0
            while j < len(temp[2:])/2:
                if temp[2*j+3]=='1':
                    friends.append(temp[2*j+2])
                    friends.append(temp[2*j+3])
                else:
                    nofriends.append(temp[2*j+2])
                    nofriends.append(temp[2*j+3])
                j = j+1
            if len(friends)>0 and len(nofriends)>0:
                net_wf.write(temp[0]+'\t'+temp[1]+'\t'+str(int(len(friends)/2))+'\t'+str(int(len(nofriends)/2))+'\t'+'\t'.join(friends)+'\t'+'\t'.join(nofriends)+'\n')
            elif len(friends)==0 and len(nofriends)>0:
                net_wf.write(temp[0]+'\t'+temp[1]+'\t'+str(int(len(friends)/2))+'\t'+str(int(len(nofriends)/2))+'\t'+'\t'.join(nofriends)+'\n')
            elif len(nofriends)==0 and len(friends)>0:
                net_wf.write(temp[0]+'\t'+temp[1]+'\t'+str(int(len(friends)/2))+'\t'+str(int(len(nofriends)/2))+'\t'+'\t'.join(friends)+'\n')
            elif len(nofriends)==0 and len(friends)==0:
                net_wf.write(temp[0]+'\t'+temp[1]+'\t0\t0\n')
            else:
                logging.error('if you see this ERROR message, plz check the code!!!')
    logging.info('save result to file %s end.'%to_file_name)

def main(args):
    start_time = time.time()
    dealData(args.input_file_name,args.output_file_name)
    end_time = time.time()
    print('End...\nThe program is running for %.2f seconds'%(end_time-start_time))

if __name__ == '__main__':
    args = parameter_parser()
    main(args)
