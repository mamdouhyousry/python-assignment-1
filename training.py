milk = 30
cheees=90
almond=100

money= 300

total_cost=milk+cheees+almond

print("total cost = ",total_cost)
print("money = ",money)
if  total_cost<=money:
    money_left= money-total_cost
    print("you have enough money, money = ",money_left)
else:
    money_needed=total_cost-money
    print("you need more money . you need ",money_needed,"more ")
