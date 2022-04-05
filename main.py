
'''
Урок 1
У нас есть список покупок и мы хотим понять
сколько денег нам с собой брать.
У нас есть бумажные купюры: 500, 100, 50
Есть монеты: 10, 5, 1
Нужно вывести сколько каждого типа нам нужно.
'''

'''shop_item_str = input ("insert item cost: ")
shop_item = float(shop_item_str)
print(shop_item)
print(type(shop_item_str), type(shop_item))'''
'''item_number > 0:
    shop_item = float(input("insert itrm cost: "))
    total_pitem_number = 10
total_price = 0
while rice +=shop_item
    print (item_number)
item_number -=1
print(shop_item)'''

'''shop_item_str = input("insert item cost:")
shop_item = float(shop_item_str)
print(shop_item)
print(type(shop_item), type(shop_item))'''

'''item_number = 10
total_price = 0
while item_number > 0:
    shop_item = float(input("insert item cost:"))
    total_price +=shop_item
    item_number -= 1 #item_number = item_number - 1
print(total_price)'''

'''случай с ограничением на сумму
left_money = 420
total_price = 0
while total_price <= 420:
    shop_item = float(input("insert item cost: "))
    if (left_money - shop_item) > 0:
      total_price += shop_item
      left_money = 420 - total_price
    elif (left_money - shop_item) == 0:
      total_price +=shop_item
      left_money =420 - total_price
      break
    else:
        print("oops , no money :(")
    print("you still have: ", left_money)
print("total price", total_price)'''


item_number = 2
total_price = 0
for i in range(item_number): # range (start, end, step)
    total_price += float(input("insert item cost:"))
print(total_price)
rub_500 = total_price // 500
left_money = total_price % 500
print("500 rub: " + str(rub_500) + "left: " + str(left_money))
#print(rub_20, left_money)



