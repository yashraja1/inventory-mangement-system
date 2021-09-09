fd = open('record.json', 'r')
t = fd.read()
fd.close()

fd = open('record.json','w')
fd.write(t)
fd.close()

sales = {}

sales = json.dumps(sales)

fd = open("sales.json", 'w')
fd.write(sales)
fd.close()

import json
import time
# Loading Inventory and Converting it to Dictionary
fd = open('record.json','r')
t = fd.read()
fd.close()
dct = json.loads(t)

# Loading Sales and Converting it to Dictionary
fd = open("sales.json", 'r')
sl = fd.read()
fd.close()
sales = json.loads(sl)


# Displaying Menu
print("**********************************************")
for i in dct.keys():
  print(i, dct[i])

print("******************************************\n")

# Taking Input from User to Enter what he/she wants to purchase
ui_prod  = str(input("Enter the product_Id: "))
ui_quant = int(input("Enter the quantity: "))


if (ui_prod in dct.keys()):                                                     
    if (dct[ui_prod]['qn'] >= ui_quant):                                        
      print("Name:",dct[ui_prod]['name'])
      print("Price:",dct[ui_prod]['pr'])
      print("Quantity:", ui_quant)
      print("------------------------------")
      print("Billing Amount:", dct[ui_prod]['pr'] * ui_quant)

      dct[ui_prod]['qn'] = dct[ui_prod]['qn'] - ui_quant                        

      sales[str(len(sales)+1)] = {'prod_id' : ui_prod,                          
                                  "time_pr" :  time.ctime(), 
                                  'bill' : dct[ui_prod]['pr'] * ui_quant, 
                                  'qn' : ui_quant, 
                                  'pr' : dct[ui_prod]['pr'], 
                                  'pr_name' : dct[ui_prod]['name']}


    else:                                                                       
      print("Sorry, We are not having that much of quantity.")
      print("We're only having",dct[ui_prod]['qn'],"quantity.")
      print("Would you like to purchase or not (Y/N)")
      ch = str(input("Y/N"))

      if (ch == "Y"):                                                          
        print("Name:",dct[ui_prod]['name'])
        print("Price:",dct[ui_prod]['pr'])
        print("Quantity:", dct[ui_prod]['qn'])
        print("------------------------------")
        print("Billing Amount:", dct[ui_prod]['pr'] * dct[ui_prod]['qn'])

        dct[ui_prod]['qn'] = 0                                                  

        sales[str(len(sales)+1)] = {'prod_id' : ui_prod,                        
                                    "time_pr" :  time.ctime(), 
                                    'bill' : dct[ui_prod]['pr'] * dct[ui_prod]['qn'], 
                                    'qn' : dct[ui_prod]['qn'], 
                                    'pr' : dct[ui_prod]['pr'], 
                                    'pr_name' : dct[ui_prod]['name']}

      else:                                                                     
        print("Thankyou!")

else:                                                                           
  print("------------------------------")
  print("Product doesn't exist!")
  print("Please enter a valid product id")
  print("------------------------------")



sl = json.dumps(sales)                                                          
fd = open('sales.json','w')
fd.write(sl)
fd.close()

print("------------------------------")
print("Data Updated in Sales File!")

js = json.dumps(dct)                                                            
fd = open('record.json','w')
fd.write(js)
fd.close()

print("Data Updated in Inventory File!")