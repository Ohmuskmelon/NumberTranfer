# pan = 0
# zhong = "零壹贰叁肆伍陆柒捌玖拾佰仟万亿元整"
# shuzi = "0123456789"
def pancuo(s,shuzi,zhong):
    p1 = 1
    p2 = 1
    for i in s :
        if zhong.find(i)==-1 : p1=0
    for i in s :
        if shuzi.find(i)==-1 : p2=0

    if p1 and p2 : return 0
    elif p1 == 0 and p2 == 0: return 0 

    if p1 == 1 : return 2
    else : return 1