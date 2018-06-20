"""
Question: Consider a list in Python which includes prices of all the items in a store.
Build a function to discount the price of all the products by 10%.
Use map to apply the function to all the elements of the list so that all the product prices are discounted.
"""

items = [10, 20, 30, 40, 50]

def discount(x):
    x -= x*0.10
    return x

result = list(map(discount,items))
print (result)