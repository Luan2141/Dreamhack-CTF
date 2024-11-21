def split_into_chunks(data, chunk_size):
    """Tách dữ liệu thành các phần có kích thước cố định"""
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# Đọc file nhị phân và tách thành các phần 8 byte
with open("out.bin", "rb") as f:
    content = f.read()

# Kích thước của mỗi phần (8 byte)
chunk_size = 8

# Tách dữ liệu thành các phần 8 byte
chunks = split_into_chunks(content, chunk_size)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def decrypt(ciphertext, v11, v10):
    # Tính phi(n)
    phi = v10 - 1  # Đây chỉ là giả định đơn giản, phi(n) thực tế cần biết p và q
    
    # Tìm khóa bí mật d
    d = mod_inverse(v11, phi)
    
    # Giải mã dữ liệu
    return pow(ciphertext, d, v10)

# Các tham số
v11 = 201326609
v10 = 18241529418349138301

for chunk in chunks:
    # Chuyển đổi khối nhị phân thành số nguyên
    ciphertext = int.from_bytes(chunk, byteorder='little')
    
    # Giải mã khối dữ liệu
    plaintext = decrypt(ciphertext, v11, v10)
    
    # Chuyển đổi số nguyên đã giải mã trở lại thành nhị phân
    decrypted_chunk = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, byteorder='little')
    
    # In nội dung đã giải mã
    for byte in decrypted_chunk:
        print(byte, end=" ")
    print()  # In dòng mới sau mỗi khối
