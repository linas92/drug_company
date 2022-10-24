from sqlalchemy.orm import sessionmaker
from drugs import engine, Customer, Cashier, Company, Vitamin

session = sessionmaker(bind=engine)()

def create_object(object_class, **kwargs):
    object = object_class(**kwargs)
    session.add(object)
    session.commit()
    return object

if __name__ == "__main__":
    while True:
        print("==================================================================================")
        print("Use your keys to insert data:")
        print("1 - Customers name")
        print("2 - reviews customers n stuff")
        print("3 - ")
        print("==================================================================================")
        pasirinkimas = int(input())
        if pasirinkimas == 1:
            create_object(
                Customer, 
                name = input("Enter the customers name: "), 
                last_name = input("Enter the customers last name: "), 
                phone_number = int(input("Enter the customers phone number: ")),
            )
        if pasirinkimas == 2:
