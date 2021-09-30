from cryptography.fernet import Fernet

#Membaca/Memanggil Kunci Dari kunci.txt
file = open('kunci.txt', 'rb')
key = file.read()
file.close()

#Membaca file pesan.txt
with open('pesan.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Output pesanencrypted.txt
with open('pesanencrypted.txt', 'wb') as f:
    f.write(encrypted)
