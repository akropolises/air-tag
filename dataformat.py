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

with open("data.csv", "r", encoding= "utf_8") as f:
    all = f.readlines()
with open("data.csv", "w", encoding= "utf_8") as g:
    for p in all:
        # p = p.replace("2./","2.7")
        # g.write(p)
        a,b,c,d = p.split(",")
        a,b,c = map(moreThan10,(a,b,c))
        d = moreThan10forD(d)
        ret = str(a)+","+str(b)+","+str(c)+","+str(d)
        g.write(ret)