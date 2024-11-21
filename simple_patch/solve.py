s = bytearray([0] * 40)  # Khởi tạo mảng bytes với 40 phần tử

s[0:8] = int.to_bytes(0xBEBDDDE33E7B4844, 8, byteorder='little')
v4 = 0xB9B58DB638482980
v5 = 0xEDBC8FBA6D1C7CDD
v6 = 0xEAEE80E36D4D7BDE
v7 = 2098998927
v8 = 0

for i in range(32):
    s[i + 3] ^= s[(i % 8)-8]  # Sử dụng chỉ số của mảng s, không làm cho nó âm

print(s)
