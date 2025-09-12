
def check_prime(num):
    if num<=1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for x in range(3,int(num**0.5)+1,2):
        if num%x==0:
         return False



print(check_prime(2))

def calc(x,y,prosess):
    if prosess =="add":
        return x+y
    elif prosess =="subtarct ":
        return x-y
    elif prosess =="multibly ":
        return x*y
    elif prosess == "divide ":
        if y ==0:
            return "error not devisable "
        return x/y
    else: return "unkown prosess"

print(calc(4,4,"add"))