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
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )

    session = Session(engine)

    state = session.query(State).order_by(State.id).first()
    print(f"{state.id}: {state.name}" if state is not None else "Nothing")

    session.close()
