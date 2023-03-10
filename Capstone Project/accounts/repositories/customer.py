import psycopg2
from accounts.models.address import Address
from accounts.models.customer import Customer

class CustomerRepository():
    DB_NAME = "capstone"
    DB_USER = "postgres"
    DB_PASS = "password"
    DB_HOST = "capstonecohort1team1db.ckokfd9swhyk.us-west-2.rds.amazonaws.com"
    #DB_HOST = "localhost"

    def insert(self, customer: Customer):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO customer(FirstName, LastName, AddressID, Email) VALUES
                (%(first)s, %(last)s, %(address)s, %(email)s)
                RETURNING id
                """, {'first': customer.first_name, 'last': customer.last_name, 'address': customer.address.id, 'email':customer.email})
                customer.id = cursor.fetchone()[0]
                return customer
    
    def delete(self, id):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                DELETE FROM customer WHERE id=%(id)s
                """, {'id': id})
    
    def get_by_id(self, id):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT * FROM customer WHERE id=%(id)s
                """, {'id': id})
                row = cursor.fetchone()
                if row:
                    addy = Address(id=row[3], address='', city='', state='', zip_code='')
                    return Customer(id=row[0], first_name=row[1], last_name=row[2], address=addy, email=row[4])
                return None