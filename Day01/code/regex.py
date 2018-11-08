import re

pattern = r'(\w+):(\d+)'
s='zhang:1994 li:1993'

#re直接调用
# l = re.findall(pattern,s)
# print(l)


#compile调用
regex = re.compile(pattern,flags=0)
l = regex.findall(s,pos=0,endpos=12)
print(l)

l1 = re.split(r'\s+','Hllo world')
print(l1)

a = re.sub(r'\s+','##','hello world china heiheihei',2)
print(a)