def moreThan10(a):
    ret = a
    if len(a) == 2:
        ret = a[:1] + "." + a[1:]
    return ret

def moreThan10forD(d):
    ret = d
    if len(d) == 3:
        ret = d[:1] + "." + d[1:]
    return ret

def trycatch(a):
    try:
        a = float(a)
        return a
    except:
        if a != "" and a != "\n":
            s.add(a)
            return 0
        return -1
s = set()
with open("data.csv", "r", encoding= "utf_8") as f:
    all = f.readlines()
# with open("data.csv", "w", encoding= "utf_8") as g:
    for idx,p in enumerate(all):
        # p = p.replace("2./","2.7")
        # g.write(p)
        a,b,c,d = p.split(",")
        # a,b,c = map(moreThan10,(a,b,c))
        # d = moreThan10forD(d)
        # ret = str(a)+","+str(b)+","+str(c)+","+str(d)
        # g.write(ret)
        a,b,c,d = map(trycatch,(a,b,c,d))
        if not (a and b and c and d):
            print(idx+1,a,b,c,d)
print(s)