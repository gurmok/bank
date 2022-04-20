import pymysql


class DB:
    def __init__(self):
        self.host = 'xxx.xxx.xxx.xxx'
        self.port = 00000
        self.user = 'xxx'
        self.password = 'xxx'
        self.db_name = 'xxx'

        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.db_name,
            charset='utf8'
        )

    def __del__(self):
        self.db.close()

    def get(self, fields=None, userid=None):
        try:
            if fields is None:
                fields = '*'  
            else:
                fields = ",".join(fields)

            if userid is None:
                sql = f'select {fields} from PI'
            else:
                sql = f"select {fields} from PI where userid='{userid}'"

            with self.db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                data = cursor.fetchall()

            return data

        except Exception as e:
            print(e.__str__())
            return None

    def post(self, values):
        try:
            values_str = f"'{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}', {values[4]}"
            sql = f"insert into PI (userid, password, name, age, gender) values ({values_str})"
            with self.db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                self.db.commit()

            return True

        except Exception as e:
            print(e.__str__())
            return False

    def put(self, filed, value, userid):
        try:
            sql = f"update PI set {filed}={value} where userid='{userid}'"
            with self.db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                self.db.commit()

            return True

        except Exception as e:
            print(e.__str__())
            return False

