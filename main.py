#module name: main
import read
import purchase
import write
again="Y"
while again.upper()=="Y":
    a=read.read_file()
    b=purchase.purchase(a)
    write.over_write(a,b)
    again=input("\nDoes the customer wants to buy more product? ")
print("\nThank you for shopping from our store!!")
print("Please check your invoice for your shopping details, \nWhich we created in stxt file format for you.")