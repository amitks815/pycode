import re
with open ("file.txt") as f:
    content=f.read()
    print(content)
pattern=re.compile(r'[A-za-z0-9.]+@[A-za-z0-9]+.[A-za-z]+')
matches=pattern.finditer(content)
for match in matches:
    print(match.group(0))



pattern=re.compile('(\d{1,3}\.){3}\d{1,3}')

matches=pattern.finditer(content)
for match in matches:
    print(match.group(0))

