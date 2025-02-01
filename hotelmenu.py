menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':30,
}
print('Welcome to our resturant, Here\'s the menu :')
for key in menu:
  print(f"{key}:Rs {menu[key]}")
total_order=0
item=input("enter the iteam you want to order :")
if item in menu:
   
    total_order=total_order+menu[item];
    print(f"{item} added sucessfully")
else:
    print(f"{item} is not available in our resturant")



message='yes'
while message!='no':

   # if message=='yes':
        item_2=input("enter the item you want to order :");
        total_order=total_order+menu[item_2]
        print(f"{item_2} added sucessfully")
        #print(f"your bill is {total_order}")
        message=input("Do you want to continue order?(yes/no) :")
print(f"your bill is {total_order}")
        
