import re
string="I am doing work with dedication and I know it will pay off"
s= re.findall("am", string)
print(s.start[0])
