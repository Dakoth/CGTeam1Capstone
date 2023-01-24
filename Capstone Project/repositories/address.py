import psycopg2
from accounts.models.address import Address

class AddressRepository():
    DB_NAME = "Address"
    DB_USER = "postgres"
    DB_PASS = "password123"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print("Connected to DB")
    except:
        print("Unable to connect to db")

    #Create cursor to allow for query execution
    cursor = conn.cursor()

    def insert(self, address: Address):
        cursor.execute('INSERT INTO Address (id, address, city, state, zipcode) \
        VALUES (?, ?, ?, ?, ?)', [address.id, address.address, address.city, address.state, address.zip_code])
        conn.commit()
        conn.close()

    def get_by_id(self, id):
        pass

if __name__ == '__main__':
    addy = Address(1, '1234 saint str', 'irvine', 'ca', 'idek')
    repo = AddressRepository()
    repo.insert(addy)