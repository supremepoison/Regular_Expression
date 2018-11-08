import re
import sys

port = sys.argv[1]
print(port)

f = open('/home/tarena/AID1808/RegularExpression/Day02/code/1.txt')
while True:
    data = ''
    for line in f:
        if line != '\n':
            data +=line
        else:
            break
    #说明已经读到文件结尾了
    if not data:
        address = 'not found the port'
    #匹配出首个单词
    try:
        PORT = re.match(r'\S+',data).group()
    except Exception as e:
        print(e)
        continue
    
    if PORT == port:
        # pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
        pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknown)'
        address = re.search(pattern,data).group(1)
        break
    



print(address)