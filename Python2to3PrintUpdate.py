#coding=cp936
import  os
dir = r'D:\computer1Sci\Anaconda\Lib\site-packages\opticspy' + '\\'
for i in os.listdir(dir):
    if i.endswith('.py'):
        cacheword = []
        with open(dir+i, 'r') as f:
            for word in f.readlines():
                if word.find('print') > 0 and word.find('print') < 2:
                    word = word.replace('print ', 'print(')
                    if not word.endswith('\\'):
                        word = word.replace('\n', ')\n')
                    if 'print' in word and 'print(' not in word:
                        word = word.replace('print', 'print(')
                    print(word)
                cacheword.append(word)
        with open(dir+i, 'w') as f:
            for i in cacheword:
                f.writelines(i)
        