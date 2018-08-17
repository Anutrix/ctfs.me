def d(num):
    res = []
    q=105
    for j in range(48,120):
        print(q)
        if q<0:
            q += 256
        if q==num:
            print(q,j)
            res.append(chr(j))
        q-=32
    return res

#flag = [233, 129, 9, 5, 130, 194, 195, 39, 75, 229]
flag=['0']
r=[]
for i in range(10):
    r.append([])
for i in range(len(flag)):
    print(flag[i])
    r[i]=d(flag[i])
    #print(ord(flag[i]))
print(r)