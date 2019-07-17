

import matplotlib.pyplot as plt
import numpy as np
import json
import string
import os
import argparse

# 将数据和眼袋关键点的标签整合到一个txt中去，每行先给出图片的路径，再给出该图片对应标签的关键点坐标平均值（一共十个点），用逗号分隔



def main():

    for id in range(1,272):

        # Search id's label in label files. Print label's information.
        f1 = False
        f2 = False
        f3 = False
        if(id <= 9 and id >= 1):
            idstr = "00" + str(id)
        else:
            idstr = str(id)
        if(os.path.exists(os.path.join("./labeled_data_1_target",idstr))):
            labeldir1 = os.path.join("./labeled_data_1_target",idstr)
            f1 = True
        if(os.path.exists(os.path.join("./labeled_data_2_target",idstr))):
            labeldir2 = os.path.join("./labeled_data_2_target",idstr)
            f2 = True
        if(os.path.exists(os.path.join("./labeled_data_3_target",idstr))):
            labeldir2 = os.path.join("./labeled_data_3_target",idstr)
            f3 = True
        if(f1==False and f2==False and f3==False):
            continue
         
        imagedir = os.path.join("./raw_image",idstr)
        for dirpath,subpaths,filenames in os.walk(imagedir):
            for filename in filenames:
                
                # set the label dir according to image dir
                labelpath1 = dirpath.replace("raw_image","labeled_data_1_target").replace("\\100","")\
                                    .replace("\\300","").replace("\\白","").replace("\\黄","")
                labelpath2 = dirpath.replace("raw_image","labeled_data_2_target").replace("\\100","")\
                                    .replace("\\300","").replace("\\白","").replace("\\黄","")
                labelpath3 = dirpath.replace("raw_image","labeled_data_3_target").replace("\\100","")\
                                    .replace("\\300","").replace("\\白","").replace("\\黄","")

                # write the image dir
                name = 'eyebags.txt'
                if(os.path.exists(os.path.join(labelpath1,filename.replace(".jpg",".json"))) or \
                      os.path.exists(os.path.join(labelpath2,filename.replace(".jpg",".json"))) or \
                          os.path.exists(os.path.join(labelpath3,filename.replace(".jpg",".json")))):
                    with open(name,'a',encoding='UTF-8') as f:
                        f.writelines([(os.path.join(dirpath,filename)),": "])
                n = 0
                coor = np.zeros(shape = (10,2))

                # load the coordinates to numpy arrays

                if(os.path.exists(os.path.join(labelpath1,filename.replace(".jpg",".json")))):
                    label_name = os.path.join(labelpath1,filename.replace(".jpg",".json"))
                    n += 1
                    with open(label_name,'r',encoding='UTF-8') as f:
                        label = json.load(f)
                        i = 0
                        for shape in label["shapes"]:
                            for point in shape["points"]:
                                x = float(point[0])
                                y = float(point[1])
                                coor[i] += [x,y]
                                i += 1
                

                if(os.path.exists(os.path.join(labelpath2,filename.replace(".jpg",".json")))):
                    label_name = os.path.join(labelpath2,filename.replace(".jpg",".json"))
                    n += 1
                    with open(label_name,'r',encoding='UTF-8') as f:
                        label = json.load(f)
                        i = 0
                        for shape in label["shapes"]:
                            for point in shape["points"]:
                                x = float(point[0])
                                y = float(point[1])
                                coor[i] += [x,y]
                                i += 1
                
                if(os.path.exists(os.path.join(labelpath3,filename.replace(".jpg",".json")))):
                    label_name = os.path.join(labelpath3,filename.replace(".jpg",".json"))
                    n += 1
                    with open(label_name,'r',encoding='UTF-8') as f:
                        label = json.load(f)
                        i = 0
                        for shape in label["shapes"]:
                            for point in shape["points"]:
                                x = float(point[0])
                                y = float(point[1])
                                coor[i] += [x,y]
                                i += 1

                # calculate the average coordinates
                if(n>0):
                    coor = coor/n
                    with open(name,'a',encoding='UTF-8') as f:
                        for i in range(0,10):
                            x = coor[i][0]
                            y = coor[i][1]
                            f.writelines([str(x),",",str(y),","])
                        f.write('\n')

if __name__ == '__main__':
    main()