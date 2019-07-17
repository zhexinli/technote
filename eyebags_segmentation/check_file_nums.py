import glob
import matplotlib.pyplot as plt
import numpy as np
import json
import string
import os
import argparse

#检查各个id文件夹下的json文件数量，如果文件数量不等于20，报告错误信息

def main():
    #total = 0
    #for dirpath,subpaths,filenames in os.walk("labeled_data_1_target"):
        #if(len(filenames)>0):
            #num = len(glob.glob(os.path.join(dirpath,"*.json"))) #glob统计该目录下指定文件类型的文件数量，不包括子目录
            #if(num!=4):
                #print("The number of files({}) is wrong. Path:{}".format(num,dirpath))
            #total += num
    #print("total:{}".format(total))
    for id in range(1,272):
        if(id <= 9 and id >= 1):
            idstr = "00" + str(id)
        else:
            idstr = str(id)
        
        dirname = os.path.join("./labeled_data_1_target",idstr)
        total = sum([len(filename) for _,_,filename in os.walk(dirname)])
        if(total != 20 and total!=0):
            print("The id{}'s label 1st's number is incorrect. ({}).".format(idstr,total))
        
        dirname = os.path.join("./labeled_data_2_target",idstr)
        total = sum([len(filename) for _,_,filename in os.walk(dirname)])
        if(total != 20 and total!=0):
            print("The id{}'s label 2nd's number is incorrect. ({}).".format(idstr,total))

        dirname = os.path.join("./labeled_data_3_target",idstr)
        total = sum([len(filename) for _,_,filename in os.walk(dirname)])
        if(total != 20 and total!=0):
            print("The id{}'s label 3rd's number is incorrect. ({}).".format(idstr,total))

        
            #print(idstr,len(filename))
    
        
if __name__ == '__main__':
    main()


#num = glob.glob(pathname = './labeled_data_1_target/003/*.json')
#print(num)
#print(len(num))