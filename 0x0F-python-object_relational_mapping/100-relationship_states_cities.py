#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(engine)
    session = Session()
    

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add(new_city)
    session.commit()
    session.close()
