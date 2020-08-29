total = 0

number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number_of_item):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for ", number_of_item, " items is $", total, sep='')