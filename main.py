import string
import random

# 18 digits
digit = string.digits
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
symbols = string.punctuation
space = ' '

temp = ''

temp += random.choice(digit)
temp += random.choice(lowercase)
temp += random.choice(uppercase)
temp += random.choice(symbols)
temp += random.choice(space)

total = digit + lowercase + uppercase + symbols

length = 18

for i in range(length - 4):
    temp += random.choice(total)

temp = list(temp)
random.shuffle(temp)

password = ''
for i in temp:
    password += i

print(password)
