tmp = "D"
tmp = hex(ord(tmp))  
tmp_int = int(tmp, 16)  

result = tmp_int ^ 0x74  
values = [
    0x74, 0x78, 0x4B, 0x65, 0x77, 0x48, 0x5C, 0x69,
    0x68, 0x7E, 0x5C, 0x79, 0x77, 0x62, 0x46, 0x79,
    0x77, 0x05, 0x46, 0x54, 0x73, 0x72, 0x59, 0x69,
    0x68, 0x7E, 0x5C, 0x7E, 0x5A, 0x61, 0x57, 0x6A,
    0x77, 0x66, 0x5A, 0x52, 0x02, 0x62, 0x5C, 0x79,
    0x77, 0x5C, 0x00, 0x7C, 0x57, 0x0D, 0x0D, 0x4D,
    0x00
]

for i in values:
    character = chr((i^result))
    print(character,end="")







