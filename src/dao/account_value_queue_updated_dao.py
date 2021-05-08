import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import db_session
from src.db.models import AccountValueQueueUpdated

class AccountValueQueueUpdatedDAO():

    def get_account_value_queue_updated(self, account_value_id):
        """Returns all queue value ids where account value id matches the specified account value id."""
        return db_session.query(AccountValueQueueUpdated)

    def delete_queued_id_batch(self, account_value_ids):
        """Returns all queue value ids where account value id matches the specified account value id."""
        db_session.query(AccountValueQueueUpdated).filter(AccountValueQueueUpdated.account_value_id.in_(account_value_ids)).delete()
        db_session.commit()
        return account_value_ids

    def create_account_value_queue_updated(self, account_value_id):
        """Creates a record in the account value queue updated table. Returns the primary key."""
        queue_updated = AccountValueQueueUpdated(account_value_id=account_value_id)
        db_session.add(queue_updated)
        db_session.commit()
        return queue_updated.queue_updated_id