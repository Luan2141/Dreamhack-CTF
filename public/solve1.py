def split_into_chunks(data, chunk_size):
    
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

def decrypt(enc_data, d, N):
    dec_data = pow(enc_data, d, N)
    return dec_data


with open("cipher.bin", "rb") as f:
    content = f.read()
    
    

chunk_size = 8


enc_data = split_into_chunks(content, chunk_size)
enc_data = [int.from_bytes(chunk, byteorder='little') for chunk in enc_data]


e = 201326609
N = 4271010253
p = 65287
q = 65419
n = (p - 1) * (q - 1)


d = pow(e, -1, n)

flag=b""  

for i in enc_data:
    flag+= decrypt(i, d, N).to_bytes(4,"little")

print(flag)


 





