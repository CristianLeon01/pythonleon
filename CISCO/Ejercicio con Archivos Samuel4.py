try:
    stream=open('C:\\pythonleon\\CISCO\\himnoSoachuno.txt','r',encoding='utf-8')
    cont = 1
    line =stream.readline()
    while line !="":
        print(f"{cont} {line}")
        line =stream.readline()
        cont +=1
          
except IOError as e:
    print(e,'...')
