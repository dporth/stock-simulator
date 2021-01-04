import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import State

class StateDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_states(self):
        """Returns all states."""
        with self._db.session_scope() as session:
            return session.query(State)

    def get_state(self, state_name):
        """Returns all states that have the state name provided."""
        with self._db.session_scope() as session:
            return session.query(State).filter_by(state_name=state_name)

    def delete_state(self, state_name):
        """Deletes all records in the state table that have the state_name specified. Returns the state id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(State.state_id).filter_by(state_name=state_name)
            for row in results:
                marked_to_delete.append(row[0])
            state = session.query(State).filter_by(state_name=state_name).delete()
            session.flush()
            return marked_to_delete

    # todo return state id
    def create_state(self, state_name):
        """Creates a record in the state table with the state_name specified. Returns the state id of the new record."""
        with self._db.session_scope() as session:
            state = State(state_name=state_name)
            session.add(state)
            session.flush()
            return state.state_id

if __name__ == "__main__":
    state = StateDAO()
    # Insert state functionality
    state_name = 'California'
    print(state.create_state(state_name))

    # Get state functionality
    results = state.get_states()
    for row in results:
        print(row)

    # Delete state funcitonality
    print(state.delete_state(state_name))

    # Get a specific state
    results = state.get_state('New York')
    for row in results:
        print(row)