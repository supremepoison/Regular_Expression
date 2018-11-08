import re
# s = 'Hello World'
# pattern = r'hello'
# regex = re.compile(pattern,flags =re.I)

# s = '''hello world
# hello kitty
# hello Miky
# '''
# pattern = r'.+'
# regex = re.compile(pattern,flags = re.S)

# s = '''
# hello world
# nihao Beijing
# '''
# pattern = r'Beijing$'
# regex = re.compile(pattern,flags=re.M)

s = '''
hello world
nihao Beijing
'''
pattern = r'''hello #匹配hello
\s+ #匹配空格
world#匹配world
'''
regex = re.compile(pattern,re.X)

try:
    s = regex.search(s).group()
except:
    print('There is no matched content')
else:
    print(s)
