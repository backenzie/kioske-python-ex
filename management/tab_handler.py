from menu import products
from product_handler import get_product_by_id

def calculate_table(list):
    subtotal = 0

    for item in list:
        item_found =  get_product_by_id(item['_id'])
        subtotal += item_found['price'] * item['amount']

    return round(float(subtotal), 2)
       
    
    

    

    

    


    
