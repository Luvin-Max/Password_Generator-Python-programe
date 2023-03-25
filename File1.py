import  random

s_letter = "abcdefghijklmnopqrstuvwxyz"
b_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@₹&/\%"

i = 1
passWordS = input("number of passwords:")
print("[1] only numbers:\n[2] numbers and letters:\n[3] numbers, letters and capital letters:\n[4] numbers,symbols, letters and capital letters:")
X = input("Select the option:")
if X == 1 :
    while i < passWordS :
        use = numbers
        lenght_for_pass = input("custom password length")
        password = "".join(random.sample(use, lenght_for_pass))
        password2= "".join(random.sample(use, lenght_for_pass))
        # print("password generator"+ password)
        # print ("password generator" , password2)
        i=i+1
        myPassword = [password]
        myPassword2 = [password2]
        fo = open("passwordFile.txt","w")
        for each_line in myPassword:
            fo.writelines([each_line])
            fo.write("\n")
        #  for each_line2 in myPassword2:
        #     fo.writelines([each_line2])
        #    fo.write("\n")
        fo = open("passwordFile.txt", "r")
        print(fo.read())
        # print(myPassword)
    fo.close()
elif X == 2 :
    while i < passWordS :
        use = s_letter + numbers
        lenght_for_pass = input("custom password length")
        password = "".join(random.sample(use, lenght_for_pass))
        password2= "".join(random.sample(use, lenght_for_pass))
        # print("password generator"+ password)
        # print ("password generator" , password2)
        i=i+1
        myPassword = [password]
        myPassword2 = [password2]
        fo = open("passwordFile.txt","w")
        for each_line in myPassword:
            fo.writelines([each_line])
            fo.write("\n")
        #  for each_line2 in myPassword2:
        #     fo.writelines([each_line2])
        #     fo.write("\n")
        fo = open("passwordFile.txt", "r")
        print(fo.read())
        # print(myPassword)
    fo.close()
elif X == 3 :
    while i < passWordS :
        use = b_letter + numbers + s_letter
        lenght_for_pass = input("custom password length")
        password = "".join(random.sample(use, lenght_for_pass))
        password2= "".join(random.sample(use, lenght_for_pass))
        # print("password generator"+ password)
        # print ("password generator" , password2)
        i=i+1
        myPassword = [password]
        myPassword2 = [password2]
        fo = open("passwordFile.txt","w")
        for each_line in myPassword:
            fo.writelines([each_line])
            fo.write("\n")
        # for each_line2 in myPassword2:
        #fo.writelines([each_line2])
        #fo.write("\n")
        fo = open("passwordFile.txt", "r")
        print(fo.read())
        #print(myPassword)
    fo.close()
elif X == 4 :
    while i < passWordS :
        use = b_letter + numbers + s_letter + symbols
        lenght_for_pass = input("custom password length")
        password = "".join(random.sample(use, lenght_for_pass))
        password2= "".join(random.sample(use, lenght_for_pass))
        # print("password generator"+ password)
        # print ("password generator" , password2)
        i=i+1
        myPassword = [password]
        myPassword2 = [password2]
        fo = open("passwordFile.txt","w")
        for each_line in myPassword:
            fo.writelines([each_line])
            fo.write("\n")
        #  for each_line2 in myPassword2:
        #     fo.writelines([each_line2])
        #    fo.write("\n")
        fo = open("passwordFile.txt", "r")
        print(fo.read())
        # print(myPassword)
    fo.close()
else:
    print("That value is not found....!")
    print("chikle agene")

