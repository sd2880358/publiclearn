import re

s = r'([a-z]+) ([a-z]+)'

pattern = re.compile(s, re.I)
#忽略大小写

str = 'aaahello world wide web'
m = pattern.match('hello world wide web')


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