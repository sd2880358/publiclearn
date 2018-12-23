import re

s = r'([a-z]+) ([a-z]+)'

pattern = re.compile(s, re.I)
#忽略大小写

str = '11hello world wide web'
m = pattern.search(str,2,40)


print(s)

a = m.span(0)


print(a)

s = m.group(1)
print(s)

a = m.span(1)
print(a)

s = m.groups()
print(s)
print(type(s))