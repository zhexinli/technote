import os
# 用于剔除数据集中不是jpg的文件
for dirpath,_,filenames in os.walk('./raw_image'):
    for filename in filenames:
        filetype = filename.split('.')[1]
        if(filetype != 'jpg'):

            print("file type wrong. Path:{}".format(os.path.join(dirpath,filename)))