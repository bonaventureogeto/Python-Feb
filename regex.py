import re

# pattern = re.compile("^Hello")

# result = pattern.finditer("Welcome to Hello World. Hello World is a great place to learn Python.")

# for match in result:
#     print(match)
#     print(match.start(), match.end(), match.group())
    
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)" # + means one or more
user_input = input("Enter your email: ")

if re.search(pattern, user_input):
    print("Valid email")
else:
    print("Invalid email")