class Product:

    count_id = 0

    def __init__(self, product_name, price, stock_count, description):
        Product.count_id += 1
        self.__product_id = Product.count_id
        self.__product_name = product_name
        self.__price = price
        self.__stock_count = stock_count
        self.__description = description

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    def get_stock_count(self):
        return self.__stock_count

    def get_description(self):
        return self.__description

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_price(self, price):
        self.__price = price

    def set_stock_count(self, stock_count):
        self.__stock_count = stock_count

    def set_description(self, description):
        self.__description = description


