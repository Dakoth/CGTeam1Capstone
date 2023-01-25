import psycopg2
from accounts.models.address import Address

class AddressRepository():
    DB_NAME = "accounts"
    DB_USER = "postgres"
    DB_PASS = "password123"
    DB_HOST = "localhost"

    def insert(self, address: Address):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO public."Address" (address, city, state, zipcode) 
                VALUES (%(address)s, %(city)s, %(state)s, %(zip)s)
                RETURNING id
                """, {'address': address.address, 'city': address.city, 'state': address.state, 'zip': address.zip_code})
                address.id = cursor.fetchone()[0]
                return address

    def get_by_id(self, id):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""SELECT * FROM public."Address" WHERE id=%(id)s;""", {'id': id})
                row = cursor.fetchone()
                return Address(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4])
    
    def get_all(self):
        results = []
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT * FROM public."Address"
                """)
                rows = cursor.fetchall()
                for row in rows:
                    results.append(Address(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4]))
                return results
    
    def update(self, address: Address):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                UPDATE public."Address" SET address=%(address)s, city=%(city)s, state=%(state)s, zip_code=%(zip)s WHERE id=%(id)s
                """, {'id': address.id, 'address': address.address, 'city': address.city, 'state': address.state, 'zip': address.zip_code})
                return self.get_by_id(address.id)
    
    def delete(self, id):
        with psycopg2.connect(host=self.DB_HOST, database=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                DELETE FROM public."Address" WHERE id=%(id)s
                """, {'id': id})