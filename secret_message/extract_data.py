from dataclasses import dataclass

def read_file(name_file):
    enc_data = []
    with open(name_file, "rb") as file:  
        byte = file.read(1) 
        while byte:
            
            value = int.from_bytes(byte, byteorder='big')  
            enc_data.append(value)
            byte = file.read(1)  
    return enc_data


enc_data= read_file("secretMessage1.enc")

class fill_data:
    def __init__(self, value: str, index: int, count: str):
        self.value = value
        self.index= index
        self.count= count

def create_data(value,count):
    data=[]
    for i in range (count):
        data.append(value)       
    return data

add_value=[]
value =-1
dem =0
for i in range (len(enc_data)):
    if(enc_data[i]==value):   
        token=fill_data(value= enc_data[i],index=i+1,count=enc_data[i+1])
        add_value.append(token)
        dem+=1
    value= enc_data[i]
dec_data=[]
j=0
k=0

for i in enc_data:
   if(k<len(add_value)): 
    if(i== add_value[k].count and j == add_value[k].index):
        if(add_value[k].count>0):
            data= create_data(add_value[k].value, add_value[k].count)
        
            dec_data+= data
        
        k+=1
    else:
        dec_data.append(i)
   else:
       dec_data.append(i)
   j+=1    

print((dec_data))   
print(len(dec_data))
byte_data = bytes(dec_data)
with open("secretMessage.raw", "wb") as file:
    file.write(byte_data)




     
     
     
     



