data =[0x39, 0xFFFFFF9B, 0x2c,0xc6, 0x59,0x58,0x39,0xAB, 0xFFFFFFCE,0xc6,0x18c,0x190,0xFFFFFFDA,0x73,0x52,0x66,0xAB, 
       0xAF, 0xD9, 0xAD, 0xAE, 0xB0, 0xB2, 0xE0, 0xE2, 0xE1, 0x4f, 0x53, 0x4C, 0x53, 0x4F, 0x57, 0x83, 0x54, 0x59, 0x87, 
       0x0C, 0x13, 0x3E, 0x3B, 0x3E, 0x39, 0x3A, 0x38, 0x0D, 0x34,
0x958, 0x92e, 0xa20, 0x12f3, 0xaf0, 0x1452, 0xb94, 0x14b4, 0xa56, 0xb9a, 0x63, 0x5F, 0x8F, 0x59, 0x8C, 0x89, 0x8C, 0x55]
s=""
s += chr(0x39-0x9)
s += chr((~0xFFFFFF9B)&0xff)
s += chr(0x2c +0x4)
s+= chr(0xc6 >>1)
s+= chr(0x59-34)
s+= chr(0x58-40)
s+= chr(0x39+40)
s+= chr(57)
s += chr((~0xFFFFFFCE)&0xff)
s+= chr(0xc6 >>1)
s+= chr(0x18C >>2)
s+= chr(0x190 >>2)
s+= chr((19 - 0xFFFFFFDA)&0xff)
s+= chr(0x73-17)
s+= chr(0x52-30)
s+= chr(0x66)

test="0123456789abcdef"

for i in range (16,26):
    for j in test:
        tmp = (~ord(j)+i)&0xff
        if(tmp == data[i]):
            s+=j

for i in range (26,36):
    tmp = chr(data[i] -i  )        
    s+= tmp  

for i in range (36, 46):
    tmp = chr(data[i] +i  )        
    s+= tmp 

for i in range (46,56):
    for j in test:
        tmp = (ord(j)*i)
        if(tmp == data[i]):
            s+=j

for i in range (56,64):
    tmp = chr(data[i] +i-100  ) 
    s+= tmp
print(s)
print(len(s))

