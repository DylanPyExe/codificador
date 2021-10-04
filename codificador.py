import base64
import time
import os
import time
import webbrowser
os.system("clear")
print("encriptador base64")
time.sleep(4)
print("https://github.com/DylanPyExe")
time.sleep(3)
os.system("clear")

print("\t\t\tSiganme en github ")

#aqui si o si tenemos que poner el texto que queramos encriptar
nya = "quiero sexo contigo"
nya_bytes = nya.encode('ascii')
base64_bytes = base64.b64encode(nya_bytes)
base64_nya = base64_bytes.decode('ascii')

print(base64_nya)

time.sleep(6)

webbrowser.open("https://github.com/DylanPyExe")
#uwu
