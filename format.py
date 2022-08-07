inputFileName = "cat1_1_xyz(3000).csv"
outputFileName = "formated_cat1_1_xyz(3000).csv"
n = 3 # 平均を取る前後のデータの数。そのデータ自身を含むので奇数推奨
# ↑例えば n = 3 の場合、(1つ前のデータ、そのデータ自身、1つ後のデータ)の平均を取る

with open(inputFileName, "r", encoding= "utf_8") as f:
    points = []
    for p in f.readlines():
        a,b,c = map(float,p.split(","))
        points.append((a,b,c))
l = len(points)
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
        if x == y == z == 0:
            print("-1,-1,-1",file=g)
        else:
            print("%f,%f,%f"%(x/cnt,y/cnt,z/cnt), file=g)