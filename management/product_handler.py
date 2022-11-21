from menu import products
from collections import Counter


def get_product_by_id(id):

    for item in products:
        if item['_id'] == id:
            return item

    return []

        
def get_products_by_type(str):
    products_found = []
    
    for item in products:
        if item['type'] == str:
            products_found.append(item)

    if len(products_found) == 0:
        return []

    return products_found

def menu_report():
    media = 0
    type_product = products[0]['type']
    
    for item in products:
        media += item['price']
        if len(get_products_by_type(type_product)) < len(get_products_by_type(item['type'])):
            type_product = item['type']
    
  
    print(f'Products Count: {len(products)} - Average Price: ${round (media / len(products), 2)} - Most Common Type: {type_product}')

def add_product(products):
    if len(products) != 0:
        new_product = {
        "_id": len(products) + 2,
        "description": products.description,
        "price": products.price,
        "rating": products.rating,
        "title": products.title,
        "type": products.type   }
        products.append(new_product)
    else:
        new_product = {
        "_id": 1,
        "description": products.description,
        "price": products.price,
        "rating": products.rating,
        "title": products.title,
        "type": products.type   }

        products.append(new_product)

        return new_product
    
        
    


# Product Count: Contagem do total de produtos do menu.
# Average Price: Média dos preços de todos os produtos do menu, arredondada para 2 casas decimais no máximo.
# Most Common Type: O tipo de produto mais comum, ou seja, o tipo que contém maior quantidade de produtos no menu.





