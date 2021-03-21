import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import AccountValueQueueUpdated

class AccountValueQueueUpdatedDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_account_value_queue_updated(self, account_value_id):
        """Returns all queue value ids where account value id matches the specified account value id."""
        with self._db.session_scope() as session:
            return session.query(AccountValueQueueUpdated)

    def delete_queued_id_batch(self, account_value_ids):
        """Returns all queue value ids where account value id matches the specified account value id."""
        with self._db.session_scope() as session:
            session.query(AccountValueQueueUpdated).filter(AccountValueQueueUpdated.account_value_id.in_(account_value_ids)).delete()
            session.commit()
            return account_value_ids

    def create_account_value_queue_updated(self, account_value_id):
        """Creates a record in the account value queue updated table. Returns the primary key."""
        with self._db.session_scope() as session:
            queue_updated = AccountValueQueueUpdated(account_value_id=account_value_id)
            session.add(queue_updated)
            session.commit()
            return queue_updated.queue_updated_id