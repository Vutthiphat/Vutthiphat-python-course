name = input("Enter Your Name : ")
letters=list(name)
print(letters)

a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

A = letters.count('A')
E = letters.count('E')
I = letters.count('I')
O = letters.count('O')
U = letters.count('U')

count = a + e + i + o + u + A + E + I + O + U
count = 0 

for letters in name :
    if letters == 'a' or letters == 'A':
        count = count + 1
    if letters == 'e' or letters == 'E':
        count = count + 1
    if letters == 'i' or letters == 'I':
        count = count + 1
    if letters == 'o' or letters == 'O':
        count = count + 1
    if letters == 'u' or letters == 'U':
        count = count + 1

print("your text have ",count, "vowels")