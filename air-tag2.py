from itertools import combinations
import numpy as np
def Matrixnumber(data1,data2):
    x1,y1,z1,d1 = data1
    x2,y2,z2,d2 = data2
    xa = -2*x1+2*x2
    ya = -2*y1+2*y2
    za = -2*z1+2*z2
    wa = d1**2-d2**2-x1**2+x2**2-y1**2+y2**2-z1**2+z2**2
    return xa,ya,za,wa

def culdist(p1,p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    d = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
    return d**(1/2)



x1,y1,z1 = 0.85,3.93,0.45
x2,y2,z2 = 1.45,0.34,1.65
x3,y3,z3 = 4.08,2.85,1.7
x4,y4,z4 = 0.55,2.6,1.93

with open("data.csv", "r", encoding= "utf_8") as f:
    with open("output.csv", "w", encoding="utf_8") as g:
        for p in f.readlines():
        # for _ in range(60):
        #     p =f.readline()
            a,b,c,d = p.split(",")
            if a and b and c and d:
                try:
                    a = float(a)
                    b = float(b)
                    c = float(c)
                    d = float(d)
                except:
                    print(-1,-1,-1,file=g)
                    continue
                data1 = (x1,y1,z1,a)
                data2 = (x2,y2,z2,b)
                data3 = (x3,y3,z3,c)
                data4 = (x4,y4,z4,d)
                data = [data1,data2,data3,data4]
                B = np.zeros((6,3))
                q = np.zeros((6,1))
                for idx,iter in enumerate(combinations(range(4),2)):
                    t1,t2,t3,t4 = Matrixnumber(data[iter[0]],data[iter[1]])
                    B[idx,] = [t1,t2,t3]
                    q[idx] = [t4] 
                B_inv = np.linalg.pinv(B)
                ans = B_inv@q
                ans = [ans[0][0], ans[1][0], ans[2][0]]
                print(*ans,file=g)
            else:
                print(-1,-1,-1,file=g)