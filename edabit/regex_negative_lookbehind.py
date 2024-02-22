import re

lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = "(?<![a-z])bad cookie"

print(len(re.findall(pattern, ", ".join(lst))))
