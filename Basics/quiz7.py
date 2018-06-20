products = {"toothpaste":80, "Salt":20, "Milk":60, "sugar":45, "Dal":100}

newproduct = input ("Enter the product:")

if newproduct in products:
    print (products.get(newproduct))
else:
    print ("Product not found.")