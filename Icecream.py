menu = {
        'Vaniella':30,
        'Butterscoth':20,
        'Chocolate':50,
        'Orange':70,
        'Pineapple':100 
        
        }
print("Welcome to Ice Cream Resturant")
print("Menu\nVaniella 30Rs\nButterscoth 20Rs\nChocolate 50Rs\nOrange 70Rs\nPineapple 100Rs")
Item_1=input("Enetr the name of item you want to order=")
ordered_total=0
if Item_1 in menu:
    ordered_total+=menu[Item_1]
    print(f"Your Item {Item_1} added to your order")
else:
    print(f"You ordered item {Item_1} is not in the list")
while True:
    another_order=input("You want to order anything else (yes/no)?")
    if another_order == 'yes':
        item_2=input("Enter the Item you want to order=")
        if item_2 in menu:
            ordered_total+=menu[item_2]
            print(f"Your item {item_2} is added in your list")
        else:
            print(f"The orderd item {item_2} is not available in the menu")
    else:
        break
print(f"The total amount of items is {ordered_total}")
    

