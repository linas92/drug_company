from sqlalchemy.orm import sessionmaker
from drugs import engine, Customer, Cashier, Company, Vitamin

session = sessionmaker(bind=engine)()

def create_object(object_class, **kwargs):
    object = object_class(**kwargs)
    session.add(object)
    session.commit()
    return object

    