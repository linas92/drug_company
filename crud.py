from sqlalchemy.orm import sessionmaker
from drugs import engine, Customer, Cashier, Company

session = sessionmaker(bind = engine)()

def create_object(object_class, **kwargs):
    object = object_class(**kwargs)
    session.add(object)
    session.commit()
    return object

def view_customers():
    view_customers = session.query(Customer).all()
    for customer in view_customers:
        print(customer)

def view_cashiers():
    view_cashiers = session.query(Cashier).all()
    for cashier in view_cashiers:
        print(cashier)

def view_companies():
    view_companies = session.query(Company).all()
    for company in view_companies:
        print(company)

def delete_object(id):
    pass

if __name__ == "__main__":
    while True:
        print("==================================================================================")
        print("Key commands to manipulate data:")
        print("1 - Insert Customer name")
        print("2 - Insert Cashier name")
        print("3 - Insert Company name")
        print("4 - View Customer list")
        print("5 - View Cashier list")
        print("6 - View Company list")
        print("7 - Delete Customers data")
        print("8 - Delete Cashiers data")
        print("9 - Delete Companies data")
        print("0 - Exit program")
        print("==================================================================================")
        pasirinkimas = int(input())
        if pasirinkimas == 1:
            create_object(
                Customer, 
                name = input("Enter the customers first name: "), 
                last_name = input("Enter the customers last name: "), 
                address = input("Enter the customers address: "), 
                phone_number = int(input("Enter the customers phone number: ")),
                email = input("Enter the customers email: "),
            )
        if pasirinkimas == 2:
            create_object(
                Cashier,
                name = input("Enter the cashier name: "),
                last_name = input("Enter the cashier last name: "), 
            )
        if pasirinkimas == 3:
            create_object(
                Company,
                name = input("Enter the companies name: "),
                address = input("Enter the companies address: "), 
                phone_number = int(input("Enter the companies telephone number: ")), 
            )
        if pasirinkimas == 4:
            view_customers()
        if pasirinkimas == 5:
            view_cashiers()
        if pasirinkimas == 6:
            view_companies()
        if pasirinkimas == 7:
            delete_object()#remove customer from database
        if pasirinkimas == 8:
            delete_object()#remove cashier from database
        if pasirinkimas == 9:
            delete_object()#remove company from database
        if pasirinkimas == 0:
            print("Thank you and have an awesome day!")
            exit()