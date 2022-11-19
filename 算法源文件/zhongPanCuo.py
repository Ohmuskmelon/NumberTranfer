def zhongpancuo(s,slen,wei,shu):
    if s == "元整" :return 0
    i = 0 
    if s[slen-2]!="元":return 0
    if s[slen-1]!="整":return 0

    yy = 0
    zz = 0 
    for i in s:
        if i=="元" : yy = yy + 1
        if i=="整" : zz = zz + 1
    if yy !=1 or zz !=1 : return 0

    for i in range(0,len(s)-2):
        if s[i]==s[i+1]:
            return 0


    if wei.find(s[0])!=-1: return 0
    # while i < slen-2 :
    #     if shu.find(s[i],1)!=-1 :
    #         if wei.find(s[i+1])==-1 : return 0
    #     elif wei.find(s[i])!=-1:
    #         if shu.find(s[i-1],1)==-1:return 0
    return 2