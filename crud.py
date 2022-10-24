from sqlalchemy.orm import sessionmaker
from drugs import engine, Customer, Cashier, Company, Vitamin, Drug

session = sessionmaker(bind=engine)()

def create_object(object_class, **kwargs):
    object = object_class(**kwargs)
    session.add(object)
    session.commit()
    return object

def view_object(object):
    pass

if __name__ == "__main__":
    while True:
        print("==================================================================================")
        print("Use your keys to insert data:")
        print("1 - Customer name")
        print("2 - Cashier name")
        print("3 - Company name")
        print("4 - Vitamin name")
        print("5 - Drug name")

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
                telephone = input("Enter the companies telephone number: "), 
            )
        if pasirinkimas == 4:
            create_object(
                Vitamin,
                name = input("Enter the vitamins name: "),
            )
        if pasirinkimas == 5:
            create_object(
                Drug,
                name = input("Enter the drugs name: "),
            )







        if pasirinkimas == 13:
            exit()