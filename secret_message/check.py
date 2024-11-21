def read_file(name_file):
    enc_data = []
    with open(name_file, "rb") as file:  # Mở tệp tin ở chế độ nhị phân
        byte = file.read(1)  # Đọc 1 byte mỗi lần
        while byte:
            # Chuyển đổi byte sang giá trị nguyên
            value = int.from_bytes(byte, byteorder='big')  # 'big' hoặc 'little' tùy thuộc vào thứ tự byte của bạn
            enc_data.append(value)
            byte = file.read(1)  # Đọc byte tiếp theo
    return enc_data

def compare_files(file1, file2):
    data_a = read_file(file1)
    data_b = read_file(file2)

    min_length = min(len(data_a), len(data_b))

    for i in range(min_length):
        if data_a[i] != data_b[i]:
            print(f"Khác biệt tại vị trí {i}: {data_a[i]} != {data_b[i]}")
            print(f"Khác biệt tại vị trí {i}: {data_a[i+1]} != {data_b[i+1]}")
            print(f"Khác biệt tại vị trí {i}: {data_a[i+2]} != {data_b[i+2]}")
            return
        else :
            print(f"giống nhau tại vị trí {i}: {data_a[i]} = {data_b[i]}")
    if len(data_a) != len(data_b):
        print(f"Hai tệp tin có độ dài khác nhau. Tệp tin thứ nhất có độ dài {len(data_a)}, tệp tin thứ hai có độ dài {len(data_b)}")
    else:
        print("Hai tệp tin giống nhau hoàn toàn.")

# Sử dụng hàm để so sánh hai tệp tin
compare_files("secretMessage.enc", "secretMessage1.enc")
