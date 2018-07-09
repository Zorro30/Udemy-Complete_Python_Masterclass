products = {"toothpaste":80, "Salt":20, "Milk":60, "sugar":45, "Dal":100}

print ("You can find prices of these commodities:{}".format([*products]))

newproduct = input ("Enter the product to know the price:")

if newproduct in products:
    print (products.get(newproduct))
else:
    print ("Product not found.")
    dec = input ("You wish to add, press yes otherwise no?")
    if dec == 'yes':
        name = input ("Enter the comodity:")
        price = int (input ("Enter the price if you know:"))
        products[name] = price
        print ("Your commodity is added for future use. {}".format(products))
    else:
        print ("Thank you for your precious time!")
        exit 
