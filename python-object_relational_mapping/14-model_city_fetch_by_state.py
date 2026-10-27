#!/usr/bin/python3

"""
queries a class that represents a city
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )

    session = Session(engine)

    states = (session.query(State.name, City.id, City.name)
              .join(City, City.state_id == State.id)
              .order_by(City.id)
              .all())
    for state_name, city_id, city_name in states:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
