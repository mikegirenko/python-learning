import re
txt = " alice15@gmail.com "
pattern = "[^a-zA-Z0-9 ]"
print(re.findall(pattern, txt))
