from math import degrees,radians,acos
def rrdot(vec1,vec2):
    x1,y1,z1 = vec1
    x2,y2,z2 = vec2
    r1 = (x1**2 + y1**2 + z1**2)**(1/2)
    r2 = (x2**2 + y2**2 + z2**2)**(1/2)
    dot = x1*x2 + y1*y2 + z1*z2
    return r1,r2,dot

inputFileName = "cat1_1_xyz(3000).csv"
outputFileName = "formated_" + inputFileName
cat = "cat" in inputFileName # cat:True, human:False
# ↑outputFileNameは自動でinputFileNameの頭に"formated_"を付けたものになります(嫌だったら従来通り変えてください)
# ↑inputFileNameに"cat"が含まれていれば　z < 2.4、そうでなければ人間のデータと見なし　z < 1.5のみを採用します

n = 3 # 平均を取る前後のデータの数。
# ↑例えば n = 3 の場合、(1つ前のデータ、そのデータ自身、1つ後のデータ)の平均を取る

theta_th = 30 # 角度の閾値
ratio_th = 2 # 比率の閾値
length_th = 0.3 # 長さの閾値
thModeisratio = True # 外れ値認定の閾値を比率)(ratio_th)で取るならTrue, 長さ(length_th)で取るならFalse


with open(inputFileName, "r", encoding= "utf_8") as f:
    points = []
    for p in f.readlines():
        a,b,c = map(float,p.split(","))
        d = 2.4 if cat else 1.5
        if 0 < a < 4.2 and 0 < b < 4.2 and 0 < c < d:
            points.append((a,b,c))
        else:
            points.append((-1,-1,-1))
l = len(points)
for i in range(1,l-1):
    x0,y0,z0 = points[i-1]
    x1,y1,z1 = points[i]
    x2,y2,z2 = points[i+1]
    if -1 in (x0,x1,x2):
        continue
    vec1 = (x1-x0,y1-y0,z1-z0)
    vec2 = (x2-x1,y2-y1,z2-z1)
    r1,r2,dot = rrdot(vec1,vec2)
    if 0 in (r1,r2):
        continue
    theta = acos(dot/(r1*r2))
    theta = abs(degrees(theta)-180)
    if theta < theta_th:
        if thModeisratio and max(r1,r2)/min(r1,r2) < ratio_th:
            points[i] = (-1,-1,-1)
        elif not thModeisratio and min(r1,r2) > length_th:
            points[i] = (-1,-1,-1)

with open(outputFileName, "w", encoding="utf_8") as g:
    for i in range(l):
        cnt = 0
        x = y = z = 0
        for j in range(n):
            idx = i - n//2 + j
            if 0 <= idx < l:
                a,b,c = points[idx]
                if a == b == c == -1:
                    continue
                if n%2 == 0 and j in (0,n-1): # nが偶数の時は一番遠い2点は半分の重みにする必要があるらしい
                    x += a/2
                    y += b/2
                    z += c/2
                    cnt += 1
                else:
                    x += a
                    y += b
                    z += c
                    cnt += 1
        if cnt == 0:
            print("-1,-1,-1",file=g)
        else:
            print("%f,%f,%f"%(x/cnt,y/cnt,z/cnt), file=g)