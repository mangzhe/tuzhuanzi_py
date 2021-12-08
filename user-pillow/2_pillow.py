#/usr/bin/python
#author: mangzhe
#-*- coding : utf-8 -*-
from PIL import Image

def rgbto(r,g,b,char_list):
    #rgb to 灰度值
    hui=int( ( r + g + b ) / 3)
    digital = int( hui * char_list.len / 256 )
    return digital


char_list=list("☑✔☐☒✘♥♠♤♂♀★☆※卐■□◆◇▲△●○◎⊕⊙«»큐〓㊚㊛囍㊒㊖")


tu=Image.open('test.png')

print(tu.width)
print(tu.height)
print(tu.mode)
print( * tu.getpixel((409,365))[:3])


