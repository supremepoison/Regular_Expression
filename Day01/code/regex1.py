import re

pattern = (r'\d+')
s = '2008事情多，08奥运，512地震'

it = re.finditer(pattern,s)

for i in it:
    #match 对象group函数说去匹配内容
    print(i.group())
try:   
    obj = re.fullmatch(r'\w+','hello1993')
    print(obj.group())
except AttributeError as e:
    print(e)

obj = re.match(r'[A-Z]\w+','Hello world')
print(obj.group())

obj = re.search(r'\d+',s)
print(obj.group())