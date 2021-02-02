# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:58:51 2020

@author: Xingyuan Xu
"""
#用于切片
import cv2 as cv
 
cap =cv.VideoCapture("F:/FastAI/paper/code/gesture/video/video2/HoldpenL.mp4")
isOpened = cap.isOpened()  ##判断视频是否打开
print(isOpened)
'''
fps = cap.get(cv.CAP_PROP_FPS)  ##获取帧率
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))   ###获取宽度
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))   ###获取高度
print(fps,width,height)
'''
i=20986
while isOpened :
    if i ==99999:   ###只保存前十张
        break
    else:
        i= i+1
    (flag,frame)=cap.read()
    
    #print(fileName)
    if flag == True and i%5 == 0:
        fileName = "image"+str(i)+".jpg"
        cv.imwrite("F:/FastAI/paper/code/gesture/video/videooutput/output2/"+str(int(i/5))+".jpg",frame,[cv.IMWRITE_JPEG_CHROMA_QUALITY,100])  ##命名 图片 图片质量
    if flag == False:
        break
print("end!")