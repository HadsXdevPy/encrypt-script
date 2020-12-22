#code by SubangProgramer
#module
import os
try:
   import py_compile
   from py_compile import compile

except ModuleNotFound:
   os.system('pip install compile')

try:
   file=input('[+] Masukan file : ')
   compile(file, file+'c')
   print(f'[+] File sukses di encrypt file > {file}c')
except:
   pass
