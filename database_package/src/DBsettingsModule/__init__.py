"""
Database sttings
-----------------------------
This ia a kdoule that has a class for database and database settings

"""

class DataBase(object):
    """Datbase Class which is responsible for connecting to the database"""
    def __init__(self, connect_str):
        """
        This ia a connection string that connects to an sql server
        :param connect_str:
        """
        self.connect = connect_str

    def connect(self) -> True:
        """
        This method is used to connect to the datase
        :return:
        """
        print("connected to the database")
