#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    Session = sessionmaker(engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{:d}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {:d}: {}".format(city.id, city.name))

    session.close()
