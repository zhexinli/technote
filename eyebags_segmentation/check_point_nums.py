import matplotlib.pyplot as plt
import numpy as np
import json
import string
import os
import argparse

#检查每个json文件的关键点数是不是10个，不是的话报错。

def main():
    for dirpath,subpaths,filenames in os.walk("labeled_data_1_target"):
        for filename in filenames:
            labelname = os.path.join(dirpath,filename)
            #print(labelname)
            with open(labelname,'r') as f:
                label = json.load(f)
                count = 0
                for shape in label["shapes"]:
                    for point in shape["points"]:
                        x = float(point[0])
                        y = float(point[1])
                        count = count+1
                #if(count==10):
                    #print("Point number is correct.")
                if(count!=10):
                    print("Point number is wrong. Point number: {}".format(count))
                    print(labelname)
    for dirpath,subpaths,filenames in os.walk("labeled_data_2_target"):
        for filename in filenames:
            labelname = os.path.join(dirpath,filename)
            #print(labelname)
            with open(labelname,'r') as f:
                label = json.load(f)
                count = 0
                for shape in label["shapes"]:
                    for point in shape["points"]:
                        x = float(point[0])
                        y = float(point[1])
                        count = count+1
                #if(count==10):
                    #print("Point number is correct.")
                if(count!=10):
                    print("Point number is wrong. Point number: {}".format(count))
                    print(labelname)
    for dirpath,subpaths,filenames in os.walk("labeled_data_3_target"):
        for filename in filenames:
            labelname = os.path.join(dirpath,filename)
            #print(labelname)
            with open(labelname,'r',encoding='UTF-8') as f:
                label = json.load(f)
                count = 0
                for shape in label["shapes"]:
                    for point in shape["points"]:
                        x = float(point[0])
                        y = float(point[1])
                        count = count+1
                #if(count==10):
                    #print("Point number is correct.")
                if(count!=10):
                    print("Point number is wrong. Point number: {}".format(count))
                    print(labelname)
    for dirpath,subpaths,filenames in os.walk("labeled_data_1_batch_272-467_target"):
        for filename in filenames:
            labelname = os.path.join(dirpath,filename)
            #print(labelname)
            with open(labelname,'r',encoding='UTF-8') as f:
                label = json.load(f)
                count = 0
                for shape in label["shapes"]:
                    for point in shape["points"]:
                        x = float(point[0])
                        y = float(point[1])
                        count = count+1
                #if(count==10):
                    #print("Point number is correct.")
                if(count!=10):
                    print("Point number is wrong. Point number: {}".format(count))
                    print(labelname)
    
        
if __name__ == '__main__':
    main()