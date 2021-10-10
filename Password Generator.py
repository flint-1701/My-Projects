import random
import string
length=int(input("Enter the Length of password:"))
# Password=random.randrange(ascii(length))
s1=string.ascii_uppercase
s2=string.ascii_lowercase
s3=string.digits
s6=string.punctuation
s4=s1+s2+s3+s6
lis=[i for i in s4]
# print(lis)
i=0
password=""
while i<length:
    a=random.choice(lis)
    password=password+a
    i=i+1
print(f"Generated password is {password}")
