from accounts.models.address import Address
from accounts.models.customer import Customer
from accounts.models.account import Account
from accounts.repositories.address import AddressRepository

address_repo = AddressRepository()

if __name__ == '__main__':
    inserted = Address(id=23, address="asdf", city="chino", state="CA", zip_code="91710")
    address_repo.insert(inserted)
    print(address_repo.get_all())