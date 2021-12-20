#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database
"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                       argv[2],
                                                                       argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name='Louisiana')
    session.add(new)
    states = session.query(State).filter_by(name='Louisiana').first()
    print(str(states.id))
    session.commit()
    session.close()
