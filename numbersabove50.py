numbers = [1, 4, 6, 10, 15, 20, 23, 28, 31, 38, 43, 48, 54, 58, 62, 67, 74, 78, 82, 88, 91, 95, 100]
for i in numbers:
    if i > 50:
        print(i)

username = "andregordon"
password = "icantcode"
while (True):
    inputusername = input("Username: ")
    inputpassword = input("Password: ")
    if (inputusername == username and inputpassword == password):
        break