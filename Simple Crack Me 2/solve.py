arr =[ 
  0xF8, 0xE0, 0xE6, 0x9E, 0x7F, 0x32, 0x68, 0x31, 0x05, 0xDC, 
  0xA1, 0xAA, 0xAA, 0x09, 0xB3, 0xD8, 0x41, 0xF0, 0x36, 0x8C, 
  0xCE, 0xC7, 0xAC, 0x66, 0x91, 0x4C, 0x32, 0xFF, 0x05, 0xE0, 
  0xD9, 0x91] 

arr1=[ 0xDE, 0xAD, 0xBE, 0xEF]
arr2=[ 0xEF, 0xBE, 0xAD, 0xDE]
arr3=[0x11, 0x33, 0x55, 0x77, 0x99, 0xBB, 0xDD]

s="0123456789abcdef"
index =0
for j in arr:
    for i in s:
        tmp = (ord(i)^arr1[index%4])&0xff
        tmp = (tmp + 31)&0xff
        tmp = (tmp- ord("Z"))&0xff
        tmp = (tmp^arr2[index%4])&0xff
        tmp = (tmp - ord("M"))&0xff
        tmp = (tmp + 243)&0xff
        tmp = (tmp^arr3[index%7])&0xff
        if (tmp== j and index<=31):
            index+=1
            print(i,end="")
            break







