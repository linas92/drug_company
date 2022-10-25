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

def delete_object(object_class, **kwargs):
    object = object_class(**kwargs)
    session.delete(object)
    session.commit()
    return object


if __name__ == "__main__":
    while True:
        print("==================================================================================")
        print("Use your keys to insert data:")
        print("1 - Customer name\n2 - Cashier name\n3 - Company name")
        print("4 - View customer list\n5 - View cashier list\n6 - View company list")
        print("")
        print("")
        print("13 - Exit program")
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
            pass#remove customer from database
        if pasirinkimas == 8:
            pass#remove cashier from database
        if pasirinkimas == 9:
            pass#remove company from database


        if pasirinkimas == 13:
            print("Thank you and have an awesome day!")
            exit()