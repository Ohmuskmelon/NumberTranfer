from shuziPanCuo import pancuo
def numberToWord(s,shuzi,zhong,slen,shu,wei):
    pan = pancuo(s,shuzi,zhong)
    anss = ""
    ansss = 0
    # if pan == 1 :
    cnt = slen 
    pp = 0
    for i in s :
        cnt = cnt - 1
        ans = shu[int(i)-int('0')] 
        if pp >= 1 and ans != "零" : 
            anss = anss + "零" 
        if pp <=2 and ans == "零" and cnt == 4 :
            anss = anss + "万"
        if pp <=2 and ans == "零" and cnt == 8 :
            anss = anss + "亿"
        if ans == "零" : 
            pp = pp + 1
            continue
        else : pp = 0
        if pp == 0 :
            if cnt == 1 : ans = ans + "拾"
            elif  cnt == 2 : ans = ans + "佰"
            elif  cnt == 3 : ans = ans + "仟"
            elif  cnt == 4 : ans = ans + "万"
            elif  cnt == 5 : ans = ans + "拾"
            elif  cnt == 6 : ans = ans + "佰"
            elif  cnt == 7 : ans = ans + "仟"
            elif  cnt == 8 : ans = ans + "亿"
            elif  cnt == 9 : ans = ans + "拾"
            elif  cnt == 10 : ans = ans + "佰"
            elif  cnt == 11 : ans = ans + "仟"
            elif  cnt == 12 : ans = ans + "万"
        anss = anss + ans
            
    anss = anss + "元整"   
    if anss == "元整" :anss = "零元整" 
    print(anss)