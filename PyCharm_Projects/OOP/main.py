from item import Item
from phone import Phone

phone1 = Phone("Smartphone Model X", 500, 5, 2)
phone1.broken_phones = 1
phone2 = Phone("Smartphone Model Y", 700, 5)
phone2.broken_phones = 2
item = Item("Smartwatch", 100, 11)
print(item.price)
# phone2.name = "Smartphone Model Z"
phone2.name = "SMP Z"

print(phone1.total_price, end='\n\n')
print(phone2.total_price, end='\n\n')
print(Item.all)
print(Phone.all)
print(phone1.read_only_name)

phone1.send_email() # as a child class, we can access method of parent class

# item1 = Item("Ali", 11, 22)
# item1.sahibi = "Mammad" # we can add attributes later

# print(item1.total_price, end = '\n\n')

# print(Item.__dict__, end='\n\n')  # all attributes for class level
# print(item1.__dict__, end='\n\n')  # all attributes for instance level

# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.total_price)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
#
# for instance in Item.all:
#     print(instance.name)
#
# print(Item.all)

# Item.instantiate_from_csv()
# print(Item.all)
#
# print(Item.is_integer(3.0))
