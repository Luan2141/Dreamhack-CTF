result2=b"C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q"
result=  ""
rot   =   ""
for i in result2:
    result += chr(i^3)

for i in range (64):
    rot+= result[63-i]

s="0123456789abcdef"
index=0
for i in rot :
    for j in s:
        tmp = (ord(j)+13)& 0x7f
        if (tmp == ord(i) and index <=63):
            print(j,end="")
            index +=1
            break


