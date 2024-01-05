import os

from retinaface import Retinaface

'''
在更换facenet网络后一定要重新进行人脸编码，运行encoding.py。
有新的图片录入就要先进行人脸编码。人脸编码读取的face_dataset图片可以含中文
img作为预测不可以含有中文

'''
retinaface = Retinaface(1)

list_dir = os.listdir("face_dataset")
image_paths = []
names = []
for name in list_dir:
    image_paths.append("face_dataset/"+name)
    names.append(name.split("_")[0])#根据下划线分割，只会取文件的名称而没有序号

retinaface.encode_face_dataset(image_paths,names)
