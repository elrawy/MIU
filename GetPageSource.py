import urllib3
import urllib.request
import os


f = open('C:/Users/ahmed.ehab/Desktop/TA/rawy','r')
message = f.read()
Lines = message.split("\n")
Sites = []
Cat = []

print(Lines)
for i in Lines:
    if len(i)==0:
        continue
    Data = i.split("@")
    print(Data)
    Sites.append(Data[0])
    Cat.append(Data[1])
Count = 40144
for i in range(0,len(Sites)):
    if os.path.isdir("E:/TA/PageSources "+Cat[i]) is False:
        os.makedirs("E:/TA/PageSources "+Cat[i])
    http = urllib3.PoolManager()
    r = http.request('get', Sites[i])
    Data = r.data
    Data = Data.decode("utf-8")
    Count += 1
    print(Count)
    File = open("E:/TA/PageSources "+Cat[i]+"/"+str(Count)+"-"+Cat[i]+".txt","w",encoding="utf-8")
    File.write(Data)
    File.close()




