import re
str = input("Enter a sentence:")
res_str = re.sub("\s", "_", str)
print(res_str)