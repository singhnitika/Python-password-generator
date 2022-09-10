import random
chars="QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm1236547890!@#$%^&*()+][}{?/"
while 1:
    password_len =int(input("Please enter the length of the password to be generated: "))
    password_count=int(input("How many suggestion would you like: "))
    for x in range(0,password_count):
        password=""
        for x in range(0,password_len):
            password_char=random.choice(chars)
            password     = password+password_char
        print("Here is your password",password)
