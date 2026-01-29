Menu={
    "pizza": 310,
    "burger": 160,
    "coffee": 70,
    "tea": 40,
    "cake": 450,
}
cart={}

print("----Menu-----")
for item , price in Menu.items():
    print(f"{item.capitalize():7}: ₹{price}")
print("Exit(0)..")
while True:
      item=input("Enter item name:  ")
      if item =="0":
        break
      if  item in Menu:
       qty=int(input("Enter quntity of item: "))
       if item in cart:
         cart[item]["qty"]+=qty
       else:
         cart[item]={
             "price":Menu[item],
             "qty":qty
         }
      else:
       print("item not found...")
      op=input("Do you want else more?(yes/no): ").lower()
      if op !="yes":
          break
total_bill=0
print("-----------BILL------------")
for item, data in cart.items():
    item_total = data["price"] * data["qty"]
    total_bill += item_total
    print("[item] [qty ] [price]")
    print(f"{item.capitalize():7} x {data['qty']} = ₹ {item_total}")
print("--------------")
print("Total bill: ",total_bill)
    
    
        
    
    