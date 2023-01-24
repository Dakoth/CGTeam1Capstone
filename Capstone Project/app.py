from accounts.models.address import Address
from accounts.models.customer import Customer
from accounts.models.account import Account
from accounts.repositories.address import AddressRepository

if __name__ == '__main__':
    addy = Address(1, 'asdf', 'irvine', 'ca', '3213')
    repo = AddressRepository()

    repo.insert(addy)