import os
import Analysis

Count = 0
Path = "E:/Data/PageSources"
Data = os.listdir(Path)
for i in Data:
    InData = os.listdir(Path+"/"+i)
    for j in InData:
        Count += 1
        print(Count)
        InPath = Path+"/"+i+"/"+j
        Analysis.FunctionGamda(InPath,i)