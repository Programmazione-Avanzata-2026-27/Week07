from database.db_connect import DB_Connect


# Classe che si occupa di parlare con il database
class Pippo:
    def __init__(self):
        db = DB_Connect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")
