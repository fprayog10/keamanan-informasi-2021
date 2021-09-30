from cryptography.fernet import Fernet

#Membaca/Memanggil Kunci Dari kunci.txt
file = open('kunci.txt', 'rb')
key = file.read()
file.close()

#Membaca file pesanencrypted.txt
with open('pesanencrypted.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
decrypted = fernet.decrypt(data)

#Output pesanencrypted.txt
with open('pesandecrypted.txt', 'wb') as f:
    f.write(decrypted)
