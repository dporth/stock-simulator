import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import AccountValueQueueUpdated

class AccountValueQueueUpdatedDAO():

    def __init__(self):
        self._db = DBHelper()

    def create_account_value_queue_updated(self, account_value_id):
        """Creates a record in the account value queue updated table. Returns the primary key."""
        with self._db.session_scope() as session:
            queue_updated = AccountValueQueueUpdated(account_value_id=account_value_id)
            session.add(queue_updated)
            session.commit()
            return queue_updated.queue_updated_id