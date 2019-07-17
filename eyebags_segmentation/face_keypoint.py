import sys
import dlib
import matplotlib.pyplot as plt
import numpy as np
import json
import string
import os
import argparse

# 使用dlib提取人脸关键点，保存到txt文件中。

# 加载人脸检测模型
detector = dlib.get_frontal_face_detector()

# 加载人脸关键点检测模型
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
# 每行先给出图片的路径，再给出人脸框的边界坐标，再给出68个关键点坐标。

def main():
    for id in range(1,272):
        if(id <= 9 and id >= 1):
            idstr = "00" + str(id)
        else:
            idstr = str(id)
        imagedir = os.path.join("./raw_image",idstr)
        name = "keypoints.txt"
        for dirpath,subpaths,filenames in os.walk(imagedir):
            for filename in filenames:
                imgpath = os.path.join(dirpath,filename)
                print("Processing file: {}".format(imgpath))
                img = dlib.load_rgb_image(imgpath)
                
                # 检测每个人脸的边界框
                dets = detector(img, 1)

                # len(dets) 是检测到的人脸数量

                # 如果没有检测到人脸，则说明dlib识别有误，用-1标记。
                if(len(dets)==0):
                    with open(name,'a',encoding='UTF-8') as f:
                        f.writelines([(os.path.join(dirpath,filename)),", -1"])
                        f.write('\n')
                    continue
                '''
                elif(len(dets)>1):
                    max = 0
                    for i in range(1,len(dets)):
                        if(dets[i].confidence>dets[max].confidence):
                            max = i

                    d = dets[max]
                    shape = predictor(img, d)

                    # 开始写入txt
                    with open(name,'a',encoding='UTF-8') as f:
                        f.writelines([(os.path.join(dirpath,filename)),", "\
                            ,str(d.left()),", ",str(d.top()),", ", \
                            str(d.right()),", ", str(d.bottom()),", "])
                        for i in range(0,68):
                            f.writelines([str(shape.part(i)),", "])
                        f.write('\n')
                    continue
                '''
                d = dets[0]
                shape = predictor(img, d)
                # 开始写入txt
                with open(name,'a',encoding='UTF-8') as f:
                    f.writelines([(os.path.join(dirpath,filename)),", "\
                        ,str(d.left()),", ",str(d.top()),", ", \
                        str(d.right()),", ", str(d.bottom()),", "])
                    for i in range(0,68):
                        f.writelines([str(shape.part(i)),", "])
                    f.write('\n')                    
                

          
if __name__ == '__main__':
    main()
