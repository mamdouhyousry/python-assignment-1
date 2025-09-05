#task 1
temp= int(input("please enter temp "))
if temp>=30:
    print("It's a hot day. Stay hydrated!")
elif 20<=temp<=29:
    print("It's a warm day. Enjoy the weather!")
elif 10<=temp<=19:
    print("It's a cool day. Wear a jacket!")
else:
    print("It's a cold day. Stay warm!")


#######################




#task 2
num= list(range(1,21))
divasable=[]
for n in num:
    if n%3==0:
        divasable.append(n)


print("divasable nums by 3 ",divasable)


