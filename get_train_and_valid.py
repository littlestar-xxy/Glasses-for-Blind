# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:20:34 2020

@author: Xingyuan Xu
"""

path ="data/custom/images/"
for i in range (1,2245):
    if i%20 ==1:
        fw = open('F:/FastAI/paper/code/PyTorch-YOLOv3-master/data/custom/valid.txt', 'a')
        fw.write(path+str(i)+str('.jpg'))
        fw.write('\n')
    else:
        fw = open('F:/FastAI/paper/code/PyTorch-YOLOv3-master/data/custom/train.txt', 'a')
        fw.write(path+str(i)+str('.jpg'))
        fw.write('\n')