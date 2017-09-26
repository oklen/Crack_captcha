# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:26:16 2017

@author: balmy
"""

import matplotlib.pyplot as plt
import re
import numpy as np
from os import getcwd
plt.rcParams['font.sans-serif']=['SimHei']
text = ''
cwd = getcwd()
with open('\\'.join((getcwd(),'OK.txt')),'r') as f:
    text = f.readlines()
title = []
for i in text:
    if i.startswith(tuple(str(i) for i in range(10))):
        title.append(i[2:])
def wordfind(i):
    list = re.findall(r'[a-d] ([\u4e00-\u9fa5]*)',i)
    return list
choice = []
for i in text[1::2]:
    choice.append(wordfind(i))
def picgente(title,choice):
    plt.style.use('seaborn-talk')
    for num,i in enumerate(choice):
        titles = title[num]
        labels = i
        sizes = np.array([])
        for i in range(4):
            sizes = np.append(sizes,np.random.randint(20,60))
            sizes = sizes/np.sum(sizes)*100
        explode = (0,0,0,0)im
        for j in plt.style.available:
            plt.style.use(j)
            plt.rcParams['font.sans-serif']=['SimHei']
            plt.title(titles)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
            plt.savefig('\\'.join((getcwd(),titles[:-3],j)))
        break
picgente(title,choice)