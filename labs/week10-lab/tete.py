password = input("Your password :")
lengh = len(passowrd)
word = password.split('@')

if len(words) > 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else :
    left = False;
    right = False;

if lenght >= 8 and len(words ) == 2 and left == True and right == True:
    print("Your password id strong!")
else:
    print("Your password is not strong!")