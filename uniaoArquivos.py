import struct
import hashlib
import os

tamanhoHash = 17035841

def h(key):
    global tamanhoHash
    return int(hashlib.sha1(key).hexdigest(), 16) % tamanhoHash

formatoIndice = "11sLL"
estruturaIndice = struct.Struct(formatoIndice)
keyColumnIndex = 5

a = open("bolsaFamilia.csv", "r")
b = open("bolsaFamiliaAux.csv", "r")
hashA = open("bolsaFamiliaHash.dat", "r+b")
uniao = open("uniaoArquivos.dat", "a+")

uniao.write(a.readline())

while True:
    line = a.readline()
    if line == "": # EOF
        break
    uniao.write(line)

while True:
    line = b.readline()
    if line == "": # EOF
        break
    record = line.split(";")
    nisProcurado = record[keyColumnIndex].replace('"','')
    p = h(nisProcurado)
    offset = p* estruturaIndice.size
    n = 1
    while True:
        hashA.seek(offset, os.SEEK_SET)
        indexRecord = estruturaIndice.unpack(hashA.read(estruturaIndice.size))
        if indexRecord[0] == str(nisProcurado):
            break
        offset = indexRecord[2]
        if offset == 0:
            uniao.write(line)
            break
        n += 1
a.close()
b.close()
hashA.close()
uniao.close()