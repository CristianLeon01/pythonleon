from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
cont = 0
try:
    stream=open('C:\\pythonleon\\CISCO\\himnoSoachuno.txt','r',encoding='utf-8')
    line =stream.readline()

    for line in line:
        for chr in line:
            if chr.isalpha():
                cont +=1
    
    
    print(f"Esta linea {line} tiene {cont} caracteres.")
                

          
except IOError as e:
    print(e,'...')



#incompleto