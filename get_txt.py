# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:29:36 2020

@author: Xingyuan Xu
"""

import os
import os.path
import xml.dom.minidom
 
path ="F:/FastAI/paper/code/PyTorch-YOLOv3-master/data/custom/images/outputs"
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
kk= 0
strpoint = '.'
catalog = 0
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        print("---------------------------")
        print(xmlFile)
        endhere = xmlFile.index(strpoint)
        namexml = str()
        for i in range (endhere):
            namexml = namexml + xmlFile[i]
        print(namexml)
        # xml文件读取操作
        # 将获取的xml文件名送入到dom解析
        dom = xml.dom.minidom.parse(os.path.join(path,xmlFile))
        root = dom.documentElement
        # 获取标签对name之间的值
        name = root.getElementsByTagName("name")
        xmin = root.getElementsByTagName("xmin")
        ymin = root.getElementsByTagName("ymin")
        xmax = root.getElementsByTagName("xmax")
        ymax = root.getElementsByTagName("ymax")
        txtname = namexml+'.'+'txt'
        path1 = 'F:/FastAI/paper/code/PyTorch-YOLOv3-master/data/custom/images/label/'
        txtpath = path1+txtname
        print(txtpath)
        fw = open(txtpath, 'a')
        for i in range(0,len(name)):
            n = name[i]
            xmin_here = xmin[i]
            ymin_here = ymin[i]
            xmax_here = xmax[i]
            ymax_here = ymax[i]
            catalogname = n.firstChild.data 
            xmin_number = int(xmin_here.firstChild.data)
            ymin_number = int(ymin_here.firstChild.data)
            xmax_number = int(xmax_here.firstChild.data)
            ymax_number = int(ymax_here.firstChild.data)
            if catalogname == 'Pos1':
                catalog = 0
            if catalogname == 'Pos2':
                catalog = 1
            if catalogname == 'Relax':
                catalog = 2
            if catalogname == 'Tip':
                catalog = 3
            if catalogname == 'Holdpen':
                catalog = 4
            
            xcenter = str((0.5*(xmin_number+xmax_number))/1920)
            ycenter = str(0.5*(ymin_number+ymax_number)/1080)
            width = str((xmax_number-xmin_number)/1920)
            height = str((ymax_number-ymin_number)/1080)
            print(n.firstChild.data)
            print(catalog)
            fw.write(str(catalog)+' '+xcenter+' '+ycenter+' '+width+' '+height+'\n')
            
            
        kk = kk+1
print(kk)
