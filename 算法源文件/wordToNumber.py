
def wordToNumber(s,shuzi,zhong,slen,shu,wei):
    # elif pan == 2 :
    cnt = slen 
    pp = 0
    i = 0
    anss = ""
    ansss = 0
    while(i<slen) :
        if wei.find(s[i])>=0 or s[i]=="零" or s[i]=="元" or s[i]=="整": 
            i = i + 1
            continue
        res1 = shu.find(s[i])
        i = i + 1
        res2 = wei.find(s[i])
        if res2 == 0 : res1 *= 10
        elif res2 == 1 : res1 *=100
        elif res2 == 2 : res1 *=1000
        elif res2 == 3 : res1 *=10000
        elif res2 == 4 : res1 *=100000000
        if res2 <= 2 : 
            if s.find("亿",i)!=-1 : 
                res1 *=100000000
            elif s.find("万",i)!=-1:
                res1 *=10000
        i = i + 1
        ansss += res1
        #print(res1)
    print(ansss)