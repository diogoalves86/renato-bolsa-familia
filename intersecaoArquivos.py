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

b = open("bolsaFamilhaAux.csv", "r")
hashA = open("bolsaFamiliaHash.dat", "r+b")
intersecao = open("bolsaInteresecao.dat", "a+")

intersecao.write(b.readline())

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
            intersecao.write(line)
            break
        offset = indexRecord[2]
        if offset == 0:
            break
        n += 1
b.close()
hashA.close()
intersecao.close()