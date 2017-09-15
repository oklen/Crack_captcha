# coding=UTF-8
#print('下')
#a = 1
#assert a == 1
#This program is used to check the accuracy of OCR
import subprocess
import os
filename = r'D:\computer17\39714658235754.jpg'

directiory = os.listdir(r'D:\computer17\custlib\Test')
for image in  directiory:
    filename =  r'D:\computer17\custlib\Test' + '\\' + image
    result = subprocess.check_output(['tesseract', filename, 'stdout', '-l', 'lang'])
    result = result.decode('cp936')[0:-4]
    print(result)
    try:
        os.rename(filename, r'D:\computer17\custlib\Test' + '\\'+ str(result) + '.jpg')
    except:
        os.remove(filename)