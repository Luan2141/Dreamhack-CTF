from pwn import *

e = ELF('./chall')
result = e.read(e.sym['result'], 0x40*4)
result = [u32(result[i*4:i*4+4]) for i in range(0x40)]
ipt = bytearray(0x40) # 크기 0x40
ipt[:0x10] = [
    result[0] - 9, (~result[1])&0xff, result[2]+4, result[3]//2,
    result[4]-0x22, result[5]-0x28, result[6]+0x28, result[7]//3,
    (~result[8])&0xff, result[9]//2, result[10]//4, result[11]//4,
    (0x13 - result[12])&0xff, result[13]-0x11, result[14]-0x1e, result[15]
]
for i in range(0x10, 0x1a):
    ipt[i] = ~(result[i]-i)&0xff
for i in range(0x1a, 0x24):
    ipt[i] = result[i]-i
for i in range(0x24, 0x2e):
    ipt[i] = result[i]+i
for i in range(0x2e, 0x38):
    ipt[i] = result[i]//i
for i in range(0x38, 0x40):
    ipt[i] = result[i]+i-100
print('DH{' + ipt.decode() + '}')
# DH{0d0c70a91ccd9b4fda8eedc657580618c37d08dbfbdc9a426c8f9d1674e0dbf0}