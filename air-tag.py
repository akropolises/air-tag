from collections import defaultdict
from itertools import combinations
def cul2pointfrom3circle(data1,data2,data3):
    x1,y1,z1,d1 = data1
    x2,y2,z2,d2 = data2
    x3,y3,z3,d3 = data3
    # xa*x+ya*y+za*z=wa 球1-球2
    xa = -2*x1+2*x2
    ya = -2*y1+2*y2
    za = -2*z1+2*z2
    wa = d1**2-d2**2-x1**2+x2**2-y1**2+y2**2-z1**2+z2**2
    # xb*x+yb*y+zb*z=wb 球1-球3
    xb = -2*x1+2*x3
    yb = -2*y1+2*y3
    zb = -2*z1+2*z3
    wb = d1**2-d3**2-x1**2+x3**2-y1**2+y3**2-z1**2+z3**2
    # z = (-Xy*x+Wy)/Zy
    Zy = za/ya - zb/yb
    Xy = xa/ya - xb/yb
    Wy = wa/ya - wb/yb
    # y = (-Xz*x+Wz)/Yz
    Yz = ya/za - yb/zb
    Xz = xa/za - xb/zb
    Wz = wa/za - wb/zb
    # ax^2+2bx+c=0
    a = 1 + (Xz/Yz)**2 + (Xy/Zy)**2
    b = -x1 + (Xz/Yz)*(y1-Wz/Yz) + (Xy/Zy)*(z1-Wy/Zy)
    c = x1**2 + (Wz/Yz - y1)**2 + (Wy/Zy - z1)**2 - d1**2
    D = (b**2-a*c)**(1/2)
    Xans1 = -c/(b+D)
    Xans2 = -(b+D)/a
    if type(Xans1) == type(1j):
        if not containsComplexNumber:
            return 0
        Xans1 = Xans1.real
        Xans2 = Xans2.real
    Yans1 = (-Xz*Xans1 + Wz)/Yz
    Yans2 = (-Xz*Xans2 + Wz)/Yz
    Zans1 = (-Xy*Xans1 + Wy)/Zy
    Zans2 = (-Xy*Xans2 + Wy)/Zy   
    return [(Xans1, Yans1, Zans1), (Xans2, Yans2, Zans2)]

def culdist(p1,p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
    return d**(1/2)

def selectAns(sorce):
    l = len(sorce)
    if l < threshold:
        return "-1,-1,-1"
    dist = defaultdict(int)
    for i in range(l):
        for j in range(i+1,l):
            dist[(i,0,j,0)] = culdist(sorce[i][0], sorce[j][0])
            dist[(i,0,j,1)] = culdist(sorce[i][0], sorce[j][1])
            dist[(i,1,j,0)] = culdist(sorce[i][1], sorce[j][0])
            dist[(i,1,j,1)] = culdist(sorce[i][1], sorce[j][1])
    retd = 1<<32 #十分大きい数。
    retx = rety = retz = -1
    for i in range(1<<l):
        sd = 0
        bit = [i>>j&1 for j in range(l)]
        for j in combinations(range(l),2):
            sd += dist[(j[0], bit[j[0]], j[1], bit[j[1]])]
        tmpX = tmpY = tmpZ = 0
        for j in range(l):
            tmpX += sorce[j][bit[j]][0]
            tmpY += sorce[j][bit[j]][1]
            tmpZ += sorce[j][bit[j]][2]
        if sd < retd:
            retd = sd
            retx = tmpX/l
            rety = tmpY/l
            retz = tmpZ/l
    return str(retx) + "," + str(rety) + "," + str(retz)

x1,y1,z1 = 0.85,3.93,0.45
x2,y2,z2 = 1.45,0.34,1.65
x3,y3,z3 = 4.08,2.85,1.7
x4,y4,z4 = 0.55,2.6,1.93

inputFileName = "data.csv"
outputFileName = "output_nonComplex_th3.csv"
containsComplexNumber = False #複素数を使わないか、虚部を捨てて使うか
threshold = 3 #採用する実数解の組の閾値

with open(inputFileName, "r", encoding= "utf_8") as f:
    with open(outputFileName, "w", encoding="utf_8") as g:
        for p in f.readlines():
            a,b,c,d = p.split(",")
            if a and b and c and d: #空データがない場合
                try:
                    a = float(a)
                    b = float(b)
                    c = float(c)
                    d = float(d)
                except: #文字や2./などの数字出ないものがある場合
                    print("-1,-1,-1",file=g)
                    continue
                data1 = (x1,y1,z1,a)
                data2 = (x2,y2,z2,b)
                data3 = (x3,y3,z3,c)
                data4 = (x4,y4,z4,d)
                ans1 = cul2pointfrom3circle(data1,data2,data3)
                ans2 = cul2pointfrom3circle(data1,data2,data4)
                ans3 = cul2pointfrom3circle(data1,data4,data3)
                ans4 = cul2pointfrom3circle(data4,data2,data3)
                sorce = []
                for i in (ans1,ans2,ans3,ans4):
                    if i != 0: #複素数を捨てる場合0が返ってきているので含めない
                        sorce.append(i)
                ans = selectAns(sorce)
                print(ans,file=g)
            else: #空データがある場合
                print("-1,-1,-1",file=g)