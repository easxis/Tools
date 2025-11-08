import random

print("Welcome to the Password Creator!")
ss = int(input("What Type of Password Do You Need \n (1).Simple Password(Does Not Contain Serious Password Rules): \n (2).Strong Password(Contains Serious Password Rules): \n"))
pnc = int(input("Please enter the number of digits you would like to create a password with:"))
if ss == 1:
    def password_creator(pnc):
        if pnc <= 0:
            print("Please Enter a Valid Number")
        else:
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            password = ''.join(random.choice(characters) for _ in range(pnc))
            print("Your password is", password)
    password_creator(pnc)
if ss == 2:
    def password_creator(pnc):
        if pnc <= 0:
            print("Please Enter a Valid Number")
        else:
            characters = "aA)bBcC(dDe3Ef*F2gGhH&iI1%j^Jk@KlL4mM$0nNo!Op5Pq6QrRs#8StTuU7vVwW9xXyY?zZ"
            password = ''.join(random.choice(characters) for _ in range(pnc))
            print("Your password is", password)
    password_creator(pnc)
else:
    print("Please Enter a Valid Option")