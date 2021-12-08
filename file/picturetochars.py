#Author : mangzhe
#Creat time :2021/12/09
#Think of desige : no
#--------------------
from PIL import Image
import argparse



parser = argparse.ArgumentParser()

parser.description="图片转字符文件"

parser.add_argument("-p",help="图片路径")
parser.add_argument("-w",help="指定宽度",type=int,default=50)

args = parser.parse_args()


PASH = args.p

WIDTH = args.w

chars=list("💯💢♨️🚷🚯🚳🚱🔞📵🚫⭕️🛑⛔️📛📛❌㊗️🈴🈵🈹❤️🧡💛💚💙💜🖤🤍🤎💔❣️💕💞💓💗💖📗📘📙📒")


def x_y(r,g,b,alpha=256):
    if alpha==0:
        value=1
    else:
        huidu = int(( r + g + b ) /3)
        value = int(huidu * len(chars) / alpha)
    return value




def main():
    im=Image.open(PASH)
    HEIGHT=int(im.height * WIDTH / im.width)
    im = im.resize(( WIDTH,HEIGHT ), Image.NEAREST).rotate(90)
    TXT=""
    for j in range(WIDTH):
        for i in range(HEIGHT):
            TXT += chars[ x_y( *im.getpixel( (j,i) )[:3]  ) ] + " "
        TXT+="\n"

    with open("out.txt",'w') as files:
        files.write(TXT)









if __name__=='__main__':
    main()
