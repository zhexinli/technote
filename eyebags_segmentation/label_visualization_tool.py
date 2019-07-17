import matplotlib.pyplot as plt
import numpy as np
import json
import string
import os
import argparse

parser = argparse.ArgumentParser(description='By Zhexin Li')
parser.add_argument('--id', type = int, default = 204, help = 'The id number you want to start with')

def main():
    args = parser.parse_args()
    start_id = args.id
    for id in range(start_id,468):

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
            print("No label for id "+idstr+"!")
            continue
        if(f1==True):
            print("id "+idstr+" has label in label 1st")
        if(f2==True):
            print("id "+idstr+" has label in label 2nd")
        if(f3==True):
            print("id "+idstr+" has label in label 3rd")
        
        imagedir = os.path.join("./raw_image",idstr)
        #image_list = []
        for dirpath,subpaths,filenames in os.walk(imagedir):
            for filename in filenames:
                
                # Display raw image if either label exists
                labelpath1 = dirpath.replace("raw_image","labeled_data_1_target").replace("\\100","")\
                                    .replace("\\300","").replace("\\白","").replace("\\黄","")
                labelpath2 = dirpath.replace("raw_image","labeled_data_2_target").replace("\\100","")\
                                    .replace("\\300","").replace("\\白","").replace("\\黄","")
                labelpath3 = dirpath.replace("raw_image","labeled_data_3_target").replace("\\100","")\
                                    .replace("\\300","").replace("\\白","").replace("\\黄","")
                if(os.path.exists(os.path.join(labelpath1,filename.replace(".jpg",".json"))) or \
                      os.path.exists(os.path.join(labelpath2,filename.replace(".jpg",".json"))) or \
                          os.path.exists(os.path.join(labelpath3,filename.replace(".jpg",".json")))):
                    image = plt.imread(os.path.join(dirpath,filename))
                    plt.figure(figsize=(15,15))
                    plt.imshow(image)
                
                
                # Display label on the image
                if(os.path.exists(os.path.join(labelpath1,filename.replace(".jpg",".json")))):
                    label_name = os.path.join(labelpath1,filename.replace(".jpg",".json"))
                    print(label_name)
                    with open(label_name,'r') as f:
                        label = json.load(f)
                        for shape in label["shapes"]:
                            for point in shape["points"]:
                                x = float(point[0])
                                y = float(point[1])
                                plt.plot(x,y,'bo')
                if(os.path.exists(os.path.join(labelpath2,filename.replace(".jpg",".json")))):
                    label_name = os.path.join(labelpath2,filename.replace(".jpg",".json"))
                    print(label_name)
                    with open(label_name,'r') as f:
                        label = json.load(f)
                        for shape in label["shapes"]:
                            for point in shape["points"]:
                                x = float(point[0])
                                y = float(point[1])
                                plt.plot(x,y,'ro')
                if(os.path.exists(os.path.join(labelpath3,filename.replace(".jpg",".json")))):
                    label_name = os.path.join(labelpath3,filename.replace(".jpg",".json"))
                    print(label_name)
                    with open(label_name,'r') as f:
                        label = json.load(f)
                        for shape in label["shapes"]:
                            for point in shape["points"]:
                                x = float(point[0])
                                y = float(point[1])
                                plt.plot(x,y,'go')
                plt.show()
                #input()
        
        
if __name__ == '__main__':
    main()