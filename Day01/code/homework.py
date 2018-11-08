import re
f = open('/home/tarena/AID1808/RegularExpression/Day01/code/test.txt')
data = f.read()
# pattern = (r'\-\d+|\s+\d+\s+|\s+\d+%\s+|\s+\d+\.\d+\s+|\s*\d+/\d+\s*')
pattern = (r'-?\d+\.?\d*\/?-?\d*\.?\d*\%?|\b[A-Z]\S*')


# s = 'Hello world Ass'
a = re.findall(pattern,data)
print(a)

f.close()