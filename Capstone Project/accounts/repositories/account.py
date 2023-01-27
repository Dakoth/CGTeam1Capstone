import psycopg2
from accounts.models.address import Address
from accounts.models.customer import Customer
from accounts.models.account import Account

class AccountRepository():
    DB_NAME = "capstone"
    DB_USER = "postgres"
    DB_PASS = "password"
    DB_HOST = "capstonecohort1team1db.ckokfd9swhyk.us-west-2.rds.amazonaws.com"
    #DB_HOST = "localhost"

    def insert(self, account: Account):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO account("accountnumber", "customerid", currentbalance)
                VALUES (%(account_num)s, %(customer_id)s, %(balance)s)
                RETURNING ID
                """, {'account_num': account.account_number, 'customer_id': account.customer.id, 'balance': account.current_balance})
                account.id = cursor.fetchone()[0]
                return account

    def delete(self, id):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                DELETE FROM account WHERE ID=%(id)s
                """, {'id': id})

    def get_by_id(self, id):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT * FROM account WHERE ID=%(id)s
                """, {'id': id})
                row = cursor.fetchone()
                if row:
                    addy = Address(id=None, address='', city='', state='', zip_code='')
                    cust = Customer(id=row[2], first_name='', last_name='', address=addy, email='')
                    return Account(id=row[0], account_number=row[1], customer=cust, current_balance=row[3])
                return None
    
    def get_by_number(self, num):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT * FROM account WHERE accountnumber=%(num)s
                """, {'num': num})
                row = cursor.fetchone()
                if row:
                    addy = Address(id=None, address='', city='', state='', zip_code='')
                    cust = Customer(id=row[2], first_name='', last_name='', address=addy, email='')
                    return Account(id=row[0], account_number=row[1], customer=cust, current_balance=row[3])
                return None

    def get_all(self):
        results = []
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT * FROM account
                """)
                rows = cursor.fetchall()
                for row in rows:
                    addy = Address(id=0, address='', city='', state='', zip_code='')
                    cust = Customer(id=row[2], first_name='', last_name='', address=addy, email='')
                    results.append(Account(id=row[0], account_number=row[1], customer=cust, current_balance=row[3]))
                return results

    def update(self, account: Account):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                UPDATE account
                SET AccountNumber=%(num)s, CustomerID=%(custid)s, CurrentBalance=%(balance)s
                WHERE ID=%(id)s
                """, {'id': account.id, 'num': account.account_number, 'custid': account.customer.id, 'balance': account.current_balance})