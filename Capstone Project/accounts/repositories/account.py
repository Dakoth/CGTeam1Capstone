import psycopg2
from accounts.models.address import Address
from accounts.models.customer import Customer
from accounts.models.account import Account

class AccountRepository():
    DB_NAME = "accounts"
    DB_USER = "postgres"
    DB_PASS = "password123"
    DB_HOST = "localhost"

    def insert(self, account: Account):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO public."Account"(id, "accountNumber", "customerID", balance)
                VALUES (%(account_num)s, %(customer_id)s, %(balance)s)
                RETURNING id
                """, {'account_num': account.account_number, 'customer_id': account.customer.id, 'balance': account.current_balance})
                account.id = cursor.fetchone()[0]
                return account

    def delete(self, id):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                DELETE FROM public."Account" WHERE id=%(id)s
                """, {'id': id})

    def get_by_id(self, id):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT * FROM public."Account" WHERE id=%(id)s
                """, {'id': id})
                row = cursor.fetchone()
                if row:
                    cust = Customer(id=row[2], first_name='', last_name='', address=None, email='')
                    return Account(id=row[0], account_number=row[1], customer=cust, current_balance=row[3])
                return None