userinput = input("How long till the party?")
usernum = int(userinput)

if usernum < 1:
    print("Party now!!!")
else:
#for ( i = usernum i >= 1 i = i - 1)
    for i in range(usernum, 0, -1):
        print(i)
        if i == 1:
            print("Party Time!!!!!")
    
