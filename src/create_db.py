import sys
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from setting import Base
from setting import ENGINE

class Tanuki(Base):
    __tablename__="Tanuki"
    id=Column(Integer, primary_key=True)
    name=Column(String(255))
    age=Column(Integer)
    type=Column(String(255))

def main(args):
    Base.metadata.create_all(bind=ENGINE)
    
if __name__ == "__main__":
    main(sys.argv)
