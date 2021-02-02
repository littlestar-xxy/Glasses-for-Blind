# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:05:43 2020

@author: Xingyuan Xu
"""
import cv2
import glob
 
def resize(img_array, align_mode):
    _height = len(img_array[0])
    _width = len(img_array[0][0])
    for i in range(1, len(img_array)):
        img = img_array[i]
        height = len(img)
        width = len(img[0])
        if align_mode == 'smallest':
            if height < _height:
                _height = height
            if width < _width:
                _width = width
        else:
            if height > _height:
                _height = height
            if width > _width:
                _width = width
 
    for i in range(0, len(img_array)):
        img1 = cv2.resize(img_array[i], (_width, _height), interpolation=cv2.INTER_CUBIC)
        img_array[i] = img1
 
    return img_array, (_width, _height)
 
def images_to_video(path):
    img_array = []
    for i in range (131):
        kk = i+1
        filename = path+str(kk)+'.png'
    #for filename in glob.glob(path+'/*.png'):
        img = cv2.imread(filename)
        if img is None:
            print(filename + " is error!")
            continue
        img_array.append(img)
 
    # 图片的大小需要一致
    img_array, size = resize(img_array, 'largest')
    fps = 6
    out = cv2.VideoWriter('F:/FastAI/paper/code/PyTorch-YOLOv3-master/output/demo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
 
images_to_video('F:/FastAI/paper/code/PyTorch-YOLOv3-master/output/')