from DB.config import DB_SETTINGS
from DB.src.db import DB

def db():
    _db = DB(DB_SETTINGS).connect_db().create_cursor()

    return _db


res = db().get_latest_record_in_users()
print(res)