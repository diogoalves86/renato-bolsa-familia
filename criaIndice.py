import struct
import hashlib
import os

def h(key):
    global tamanhoHash
    return int(hashlib.sha1(key).hexdigest(), 16) % tamanhoHash

tamanhoHash = 17035841
formatoIndice = "11sLL"
estruturaIndice = struct.Struct(formatoIndice)
keyColumnIndex = 5
nomeArquivo = "bolsaFamilia.csv"
nomeArquivoIndice = "bolsaFamiliaHash.dat"

fi = open(nomeArquivoIndice, "wb")
registroVazioNoIndice = estruturaIndice.pack("", 0, 0)
for i in range(0, tamanhoHash):
    fi.write(registroVazioNoIndice)
fi.close()

f = open(nomeArquivo, "r")
fi = open(nomeArquivoIndice, "r+b")#hash

fi.seek(0, os.SEEK_END)
tamanhoArquivo = fi.tell()
print ("Tamanho do arquivo é: ", tamanhoArquivo)

f.readline()

recordNumber = 0
while True:
    recordNumber = f.tell()
    line = f.readline()
    if line == "": # EOF
        break
    record = line.split(";")
    p = h(record[keyColumnIndex].replace('"',''))
    fi.seek(p * estruturaIndice.size, os.SEEK_SET)
    indexRecord = estruturaIndice.unpack(fi.read(estruturaIndice.size))
    fi.seek(p * estruturaIndice.size, os.SEEK_SET)
    if indexRecord[0][0] == "\0":
        fi.write(estruturaIndice.pack(record[keyColumnIndex].replace('"',''), recordNumber, 0))
    else:
        nextPointer = indexRecord[2]
        fi.write(estruturaIndice.pack(indexRecord[0],indexRecord[1],tamanhoArquivo))
        fi.seek(0,os.SEEK_END)
        fi.write(estruturaIndice.pack(record[keyColumnIndex].replace('"',''),recordNumber,nextPointer))
        tamanhoArquivo = fi.tell()
    recordNumber += 1
f.close()
fi.close()
