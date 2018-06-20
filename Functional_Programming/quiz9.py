"""Question: Assume you want to build two functions for discounting products on a website.
Function number 1 is for student discount which discounts the current price to 10%.
Function number 2 is for additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
Depending on the situation, we want to be able to apply both the discounts on the products.
"""

def stud_discount(x):
    disc = x - x*0.10
    return disc

def add_discount(func):
    final = func - func*0.05
    return final

print (add_discount(stud_discount(100)))