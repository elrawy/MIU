import re
f = open('try.txt','r')
f2 = open('after.txt','w')
data = f.read().replace('\n','')
x = re.findall(r'<!DOCTYPE html>(.*?)</html>',data,re.DOTALL)
f2.write(str(x))
# print(x)

# myhtml = open("try.txt","r")
# for item in myhtml.split("</tag>"):
#     if "<tag>" in item:
#         print (item[item.find("<tag>") + len("<tag>"):])