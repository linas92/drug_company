from sqlalchemy import Column, Integer, String, ForeignKey, create_engine,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///data/drugs.db")
Base = declarative_base()

# susikursiu keleta klasiu ir lenteliu:
# 1 - vartotojas
# 2 - kasininkas
# 3 - kompanija
# 4 - vaistas
# 5 - isveziotojas


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)