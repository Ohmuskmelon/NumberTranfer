def jisuan(s):
    pan = 0
    zhong = "零壹贰叁肆伍陆柒捌玖拾佰仟万亿元整"
    shuzi = "0123456789"

    def pancuo():
        p1 = 1
        p2 = 1
        for i in s:
            if zhong.find(i) == -1: p1 = 0
        for i in s:
            if shuzi.find(i) == -1: p2 = 0

        if p1 and p2:
            return 0
        elif p1 == 0 and p2 == 0:
            return 0

        if p1 == 1:
            return 2
        else:
            return 1

    shu = "零壹贰叁肆伍陆柒捌玖"
    wei = "拾佰仟万亿兆元整"
    slen = len(s)
    slen = int(slen)

    def zhongpancuo():
        if s == "元整": return 0
        i = 0
        if s[slen - 2] != "元": return 0
        if s[slen - 1] != "整": return 0

        yy = 0
        zz = 0
        for i in s:
            if s[i] == "元": yy = yy + 1
            if s[i] == "整": zz = zz + 1
        if yy != 1 or zz != 1: return 0

        for i in range(0, len(s)):
            if s[i] == s[i + 1]:
                return 0;

        if wei.find(s[0]): return 0
        while i < slen - 2:
            if shu.find(s[i], 1) != -1:
                if wei.find(s[i + 1]) == -1: return 0
            elif wei.find(s[i]) != -1:
                if shu.find(s[i - 1], 1) == -1: return 0

    pan = pancuo()
    anss = ""
    ansss = 0

    if pan == 1:
        cnt = slen
        pp = 0
        for i in s:
            cnt = cnt - 1
            ans = shu[int(i) - int('0')]
            if pp >= 1 and ans != "零":
                anss = anss + "零"
            if pp <= 2 and ans == "零" and cnt == 4:
                anss = anss + "万"
            if pp <= 2 and ans == "零" and cnt == 8:
                anss = anss + "亿"
            if ans == "零":
                pp = pp + 1
                continue
            else:
                pp = 0
            if pp == 0:
                if cnt == 1:
                    ans = ans + "拾"
                elif cnt == 2:
                    ans = ans + "佰"
                elif cnt == 3:
                    ans = ans + "仟"
                elif cnt == 4:
                    ans = ans + "万"
                elif cnt == 5:
                    ans = ans + "拾"
                elif cnt == 6:
                    ans = ans + "佰"
                elif cnt == 7:
                    ans = ans + "仟"
                elif cnt == 8:
                    ans = ans + "亿"
                elif cnt == 9:
                    ans = ans + "拾"
                elif cnt == 10:
                    ans = ans + "佰"
                elif cnt == 11:
                    ans = ans + "仟"
                elif cnt == 12:
                    ans = ans + "万"
            anss = anss + ans

        anss = anss + "元整"
        if anss == "元整": anss = "零元整"

        return(anss)
    elif pan == 2:
        i = 0
        while (i < slen):
            if wei.find(s[i]) >= 0 or s[i] == "零" or s[i] == "元" or s[i] == "整":
                i = i + 1
                continue
            res1 = shu.find(s[i])
            i = i + 1
            res2 = wei.find(s[i])
            if res2 == 0:
                res1 *= 10
            elif res2 == 1:
                res1 *= 100
            elif res2 == 2:
                res1 *= 1000
            elif res2 == 3:
                res1 *= 10000
            elif res2 == 4:
                res1 *= 100000000
            if res2 <= 2:
                if s.find("亿", i) != -1:
                    res1 *= 100000000
                elif s.find("万", i) != -1:
                    res1 *= 10000
            i = i + 1
            ansss += res1
            # print(res1)
        print(ansss)
        return (ansss)
    else:
        cuowu = "输入错误"
        return(cuowu)