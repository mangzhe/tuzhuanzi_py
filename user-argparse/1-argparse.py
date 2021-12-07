#/usr/bin/python
#参考网址：
#https://www.jianshu.com/p/00425f6c0936
#https://www.cnblogs.com/shmily2018/p/11592448.html

import argparse

def Parser():
    parser = argparse.ArgumentParser()
    parser.description='喂我两个数字，我就吐出他们的积'
    parser.add_argument("-a", help="我是A",type=int ,default = 6)
    parser.add_argument("-b", help="我是B",type=int ,default = 7)
    return parser



if __name__ == '__main__':
    parser=Parser()
    args = parser.parse_args()
    print(args.a*args.b)

