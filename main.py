from management import product_handler

def main():
    print(product_handler.get_product_by_id(1))
    print(product_handler.get_products_by_type('fruit'))
    print(product_handler.menu_report())
    


if __name__ == "__main__":
    main()
