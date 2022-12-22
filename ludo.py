import random
print("WELCOME TO THE GAME ")
print("developed by - Mr. AKASH YADAV")
str1=input("Enter the name of player 1 :: ")
str2=input("Enter the name of player 2 :: ")
n=input("press any key to enter into the game :: ")
sum1=0
sum2=0
while True:
    a=random.randint(1,6)
    print("\n",str1, "it is your turn and you get the number ",a)
    sum1=sum1+a
    if sum1==20:
        print(str1,"you are winner")
        break
    b=random.randint(1,6)
    print("\n",str2,"it is your turn and you get the number ",b)
    sum2=sum2+b
    if sum2==20:
        print(str2,"you are winner")
        break
    num=int(input("do you want to continue :: press 1 for yes and press 2 for exit :: "))
    if num==1:
        continue
    else:
        if sum1<sum2:
            print(str2, "you are winner")
        elif sum1>sum2:
            print(str1, "you are winner")
        elif sum1==sum2:
            print(str1,"and", str2," both have equal score")
        break
print("thankyou")
