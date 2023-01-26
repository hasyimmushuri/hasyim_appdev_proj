from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm, CreateCustomerForm, CreateProductForm
import shelve, User, Customer, Product

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/checkOut')
def checkout_page():
    products_dict = {}
    db = shelve.open('products.db', 'r')
    products_dict = db['products']
    db.close()

    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)
    return render_template('checkoutPage.html', count=len(products_list), products_list=products_list)

# -------------------------------------------------------------------------------

@app.route('/createProducts', methods=['GET', 'POST'])
def products():
    create_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and create_product_form.validate():
        products_dict = {}
        db = shelve.open('products.db', 'c')

        try:
            products_dict = db['products']
        except:
            print("Error in retrieving products from products.db.")
        product = Product.Product(create_product_form.productName.data, create_product_form.price.data, create_product_form.stock_count.data, create_product_form.description.data)
        products_dict[product.get_product_id()] = product
        db['products'] = products_dict
        print("created new product")

        db.close()

        return redirect(url_for('retrieve_products'))
    return render_template('createProducts.html', form=create_product_form)

@app.route('/retrieveProduct')
def retrieve_products():

    products_dict = {}
    db = shelve.open('products.db', 'r')
    products_dict = db['products']
    db.close()

    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)
    return render_template('productPage.html', count=len(products_list), products_list=products_list)

@app.route('/updateProduct/<int:id>/', methods=['GET', 'POST'])
def update_product(id):

    update_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and update_product_form.validate():
        products_dict = {}
        db = shelve.open('products.db', 'w')
        products_dict = db['products']

        product = products_dict.get(id)
        product.set_product_name(update_product_form.productName.data)
        product.set_stock_count(update_product_form.stock_count.data)
        product.set_price(update_product_form.price.data)
        product.set_description(update_product_form.description.data)

        db['products'] = products_dict
        db.close()

        return redirect(url_for('retrieve_products'))
    else:
        products_dict = {}
        db = shelve.open('products.db', 'w')
        products_dict = db['products']
        db.close()

        product = products_dict.get(id)
        update_product_form.productName.data = product.get_product_name()
        update_product_form.stock_count.data = product.get_stock_count()
        update_product_form.price.data = product.get_price()
        update_product_form.description.data = product.get_description()

        return render_template('updateProducts.html', form=update_product_form)

@app.route('/deleteProduct/<int:id>', methods=['POST'])
def delete_product(id):

    products_dict = {}

    db = shelve.open('products.db', 'w')
    products_dict = db['products']

    products_dict.pop(id)

    db['products'] = products_dict
    db.close()
    return redirect(url_for('retrieve_products'))

# ---------------------------------------------------------------------------------
@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")
        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.membership.data, create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form=create_user_form)

@app.route('/retrieveUsers')
def retrieve_users():

    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)
    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)

@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):

    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_membership(update_user_form.membership.data)
        user.set_remarks(update_user_form.remarks.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.membership.data = user.get_membership()
        update_user_form.remarks.data = user.get_remarks()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):

    users_dict = {}

    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()
    return redirect(url_for('retrieve_users'))

# --------------------------------------------------------------------------------------

@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                                     create_customer_form.gender.data, create_customer_form.membership.data,
                                     create_customer_form.remarks.data, create_customer_form.email.data,
                                     create_customer_form.date_joined.data, create_customer_form.address.data)
        customers_dict[customer.get_user_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('createCustomer.html', form=create_customer_form)


@app.route('/retrieveCustomers')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)




@app.route('/updateCustomer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):

    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_membership(update_customer_form.membership.data)
        customer.set_remarks(update_customer_form.remarks.data)
        customer.set_remarks(update_customer_form.email.data)
        customer.set_remarks(update_customer_form.date_joined.data)
        customer.set_remarks(update_customer_form.address.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieve_customers'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.membership.data = customer.get_membership()
        update_customer_form.remarks.data = customer.get_remarks()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.date_joined.data = customer.get_date_joined()
        update_customer_form.address.data = customer.get_address()

        return render_template('updateCustomer.html', form=update_customer_form)



@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):

    customers_dict = {}

    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']

    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()
    return redirect(url_for('retrieve_customers'))


if __name__ == '__main__':
    app.run()