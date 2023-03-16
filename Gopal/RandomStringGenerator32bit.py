import string
import secrets
from Model import  Model

class RandomStringGenerator32bit(Model):
    def __init__(self, DB_Name, TABLE_NAME, TABLE_VALUES):
        super().__init__(DB_Name, TABLE_NAME, TABLE_VALUES)
        self.create_table()

    def unique_secret_token_generator(self):
        alphabet = string.ascii_letters + string.digits

        while True:
            token = ''.join(secrets.choice(alphabet) for i in range(10))
            if (self.insert_data_in_table(token)):
                print("TOKEN= %s" % token)
                break
        return token


test = RandomStringGenerator32bit("test.db","Test1", "Name")
token = test.unique_secret_token_generator()
print (token)
test.get_table_data()
test.close_connection()
