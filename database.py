import pymysql.cursors


class Database(object):
    __instance = None
    __host = None
    __user = None
    __passwd = None
    __db = None

    def __new__(cls, *args, **kwargs):
        if Database.__instance is None:
            Database.__instance = object.__new__(cls)
        return Database.__instance

    def setConnection(self, host, user, passwd, db):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db = db

    def conexion(self):
        db = pymysql.connect(host=self.__host,
                             user=self.__user,
                             passwd=self.__passwd,
                             db=self.__db,
                             autocommit=True
                             )
        return db

    def run(self, query):
        db = pymysql.connect(host=self.__host,
                             user=self.__user,
                             passwd=self.__passwd,
                             db=self.__db,
                             autocommit=True
                             )

        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute(query)

        db.close()

        return cursor
