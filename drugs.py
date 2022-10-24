from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///data/drugs.db")
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    last_name = Column("last_name", String)
    address = Column("address", String)
    phone_number = Column("phone_number", Integer)
    email = Column("email", Integer)

    def __repr__(self):
        return f"({self.id},{self.name},{self.last_name},{self.phone_number},{self.email})"


class Cashier(Base):
    __tablename__ = "cashier"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    last_name = Column("last_name", String)

    companies_id = Column("companies_id", Integer, ForeignKey("companies.id"))
    companies = relationship("Company", back_populates = "cashiers")

    customers_id = Column("customers_id", Integer, ForeignKey("customers.id"))
    customers = relationship("Customer", back_populates = "cashiers")

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.last_name})"


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    address = Column("address", String)
    telephone = Column("telephone", Integer)

    cashiers_id = Column("cashiers_id", Integer, ForeignKey("cashiers.id"))
    cashiers = relationship("Cashier", back_populates = "companies")

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.address}, {self.telephone})"


class Vitamin(Base):
    __tablename__ = "vita"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    vitamin = Column("vitamin_id", Integer, ForeignKey("vitamin.id"))

    def __repr__(self):
        return f"({self.id}, {self.name}, )"


class Drug(Base):
    __tablename__ = "drugs"
    id = Column(Integer, primary_key = True)
    name = Column("name", String)
    drug = Column("drug_id", Integer, ForeignKey("drug.id"))

    def __repr__(self):
        return f"({self.id}, {self.name}, )"


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

