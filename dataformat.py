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
        float(a)
        return True
    except:
        if a != "" and a != "\n":
            s.add(a)
            global idx
            print(idx,a)
            return False
        else:
            return True

inputFileName = "data.csv"
outputFileName = inputFileName

s = set()
with open(inputFileName, "r", encoding= "utf_8") as f:
    all = f.readlines()
with open(outputFileName, "w", encoding= "utf_8") as g:
    for idx,p in enumerate(all):
        p = p.replace("2./","2.7") #2./ -> 2.7
        a,b,c,d = p.split(",")
        A,B,C,D = map(trycatch,(a,b,c,d))
        if A and B and C and D:
            a,b,c = map(moreThan10,(a,b,c))
            d = moreThan10forD(d)
            p = str(a)+","+str(b)+","+str(c)+","+str(d)
        g.write(p)
print(s)