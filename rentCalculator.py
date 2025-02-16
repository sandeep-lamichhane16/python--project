rent=float(input("enter the total rent of the flat :"))
food=float(input("enter the amount of food ordered :"))
totalUnit=int(input("enter the total unit of electrity used :"))
perUnit=float(input("enter the price of the each unit :"))
num=int(input("enter the number of the student that  are staying in the hostel :"))

total_Amount=rent+food+totalUnit*perUnit
print(f"the total bill of the month  is {total_Amount}\n")
print(f"the bill that each person on 3 person is {total_Amount/num}")

