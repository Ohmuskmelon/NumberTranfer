s = input()
pan = 0
zhong = "零壹贰叁肆伍陆柒捌玖拾佰仟万亿元整"
shuzi = "0123456789"

from zhongPanCuo import zhongpancuo
from shuziPanCuo import pancuo
from numberToWord import numberToWord
from wordToNumber import wordToNumber
# from init import *
shu = "零壹贰叁肆伍陆柒捌玖"
wei = "拾佰仟万亿兆元整"
slen = len(s)
slen = int(slen)


def convert():
    pan = pancuo(s,shuzi,zhong)
    # 中文
    if(pan==2):
        pan =zhongpancuo(s,slen,wei,shu)
        
    if(pan==1):
        numberToWord(s,shuzi,zhong,slen,shu,wei)
    elif(pan==2):
        wordToNumber(s,shuzi,zhong,slen,shu,wei)
    elif(pan==0):
        print("输入错误")
        
convert()