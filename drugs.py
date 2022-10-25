from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///data/drugs.db")
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    last_name = Column("last_name", String)
    address = Column("address", String, unique = True)
    phone_number = Column("phone_number", Integer)
    email = Column("email", String)
    cashier = relationship("Cashier", back_populates = "customer")
    company = relationship("Company", back_populates = "customer")

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.last_name}, {self.address}, {self.phone_number}, {self.email})"


class Cashier(Base):
    __tablename__ = "cashier"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    last_name = Column("last_name", String)
    customer_id = Column("customer_id", Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates = "cashier")

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.last_name})"


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    address = Column("address", String)
    phone_number = Column("phone_number", Integer)
    customer_id = Column("customer_id", Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates = "company")
    

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.address}, {self.phone_number})"


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)