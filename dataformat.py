with open("data.csv", "r", encoding= "utf_8") as f:
    all = f.readlines()
with open("data.csv", "w", encoding= "utf_8") as g:
    for p in all[:1]:
        print(p)
        p = p.replace("2./","2.7")
        g.write(p)