#!/usr/bin/python3

"""
Makes a class that represents a state
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]),
        pool_pre_ping=True
        )

    session = Session(engine)

    states = session.query(State).where(State.name.like(
            sys.argv[4])).order_by(State.id).all()
    if not states:
        print("Not found")
    else:
        for state in states:
            print(f"{state.id}")

    session.close()
