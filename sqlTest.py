import pymysql
from werkzeug import generate_password_hash, check_password_hash

class SQLTest:
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.passwd = 'Gareth123!'
        self.db = 'BucketList'

    def select_all_data(self):
        select_query = "select * from tbl_user"
        cursor.execute(select_query)
        records = cursor.fetchall()
        for row in records:
            print("Member Number = ", row[0], )
            print("Name = ", row[1])
            print("Email  = ", row[2])

    def select_user_data(self):
        username_string = "\"gareth.kaczkowski@gmail.com\""
        query = "select * from tbl_user where user_username = {};".format(username_string)
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            print("Member Number = ", row[0], )
            print("Name = ", row[1])
            print("Email  = ", row[2])

    def update_user_data(self):
        # ex. update password of a user
        # current SQL update method only allows updates using a primary key i.e. user_id
        username_string = "\"gareth.kaczkowski@gmail.com\""
        _password = "Gareth123!"

        _hashed_password = "\"{}\"".format(generate_password_hash(_password))
        user_id_query = "select user_id from tbl_user where user_username = {}".format(username_string)
        cursor.execute(user_id_query)
        records = cursor.fetchall()
        for row in records:
            user_id = row[0]
        
        update_query = "update tbl_user set user_password = {} where user_id = {}"\
            .format(_hashed_password, user_id)
        cursor.execute(update_query)

    def check_user_password(self):
        username_form = "\"{}\"".format("gareth.kaczkowski@gmail.com")
        _password = "Gareth123!"
        cursor.execute("SELECT user_password FROM tbl_user WHERE user_username = {};".format(username_form))
        for row in cursor.fetchall():
            if check_password_hash(row[0], _password):
                print("Password Correct")
            else:
                print("Incorrect Password")


if __name__ == "__main__":
    test = SQLTest()

    # establish a connection with the SQL database
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gareth123!', db='BucketList')
    cursor = conn.cursor()

    # select function to run here
    test.check_user_password()

    # close the connection
    cursor.close()
    conn.close()
