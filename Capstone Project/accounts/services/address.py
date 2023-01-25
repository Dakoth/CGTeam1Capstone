from accounts.models.address import Address
from accounts.repositories.address import AddressRepository

class AddressService():
    def __init__(self, address_repository: AddressRepository):
        self.product_repository = address_repository

    def add_new(self, address: Address):
        return self.product_repository.insert(address)

    def get_all(self):
        return self.product_repository.get_all()

    def get_one(self, product_number):
        return self.product_repository.get_by_number(product_number)

    def update(self, address: Address):
        return self.product_repository.update(address)