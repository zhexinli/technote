该项目为眼袋分割项目，围绕人脸眼袋、卧蚕部位的一系列任务进行预研，包括对眼袋和卧蚕的分类，对眼袋区域的分割以及对眼袋健康状态的评分等。

1 数据标注

  首先确定眼袋、卧蚕的标注规则。然后使用labelme工具对某人脸数据集进行标注。每个id有20张图片需要标注，每个图片应标注10个关键点来表示眼袋区域。每张图片由三个分别标注。
  
2 数据清理

  首先编写一个标签可视化工具label_visualization_tool.py，读取labelme生成的json文件，将关键点plot在对应的图片上。可以直观方便地逐张查看标注效果。
  
  然后编写了两个自动检错脚本check_file_nums.py和check_point_nums.py，前者可自动检测每个id的20张图片是否都被标注，如果标注的图片少于20张，则报错。后者可自动检测每个标注文件的关键点数量是否正好为10个，多标或少标都报错。
  
  然后将有错的图片重新进行手动标注，覆盖原先错误的标注文件。
  
  数据集和标签是分开存储的，但是在清理过程中有时会在数据集中不小心添加进一些json文件并且忘记删除，于是写了一个脚本find_json.py便于剔除数据集中误加的json文件。
  
3 数据处理

  写了一个脚本txt_converter.py，将数据和眼袋关键点的标签整合到一个txt中去，每行先给出图片的路径，再给出该图片对应关键点的坐标（一共10组），用逗号分隔。因为每张图片有三个标注，因此需要读取三个标注文件，将其坐标取平均后再输出到txt文件中去。
  
  同时，除了眼袋的关键点，项目还需要用到人脸关键点。使用开源的人脸关键点检测库dlib进行人脸关键点的提取。在服务器上安装dlib-with-cuda的过程如下：
  
  git clone https://github.com/davisking/dlib.git
  
  cd dlib
  
  mkdir build
  
  cd build
  
  cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1
  
  cmake --build .
  
  cd ..
  
  python setup.py install --yes USE_AVX_INSTRUCTIONS --yes DLIB_USE_CUDA
  
  在编译过程中，系统提示找不到cudnn
  
  但服务器上已经装了cudnn，因此需要手动设定路径

  在bashrc中加入path和动态库path：
  
  export LD_LIBRARY_PATH="/cm/shared/apps/cudnn/6.0/lib64:$LD_LIBRARY_PATH"
  
  export PATH="/cm/shared/apps/cudnn/6.0/include:$PATH"
  
  在python命令行下键入以下代码可用于测试是否安装成功：

  import dlib

  dlib.DLIB_USE_CUDA

  如果输入为True，则说明gpu加载成功。
