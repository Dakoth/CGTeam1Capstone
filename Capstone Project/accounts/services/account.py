from ast import Add
from audioop import add
from accounts.models.account import Account
from accounts.repositories.account import AccountRepository
from accounts.repositories.customer import CustomerRepository #f key
from accounts.repositories.address import AddressRepository # f key

class AccountService():
    def __init__(self, account_repository: AccountRepository, customer_repository: CustomerRepository,
            address_repository: AddressRepository) -> None:
        self.account_repository = account_repository
        self.customer_repository = customer_repository
        self.address_repository = address_repository

    def open_account(self, account: Account) -> Account:
        address = self.address_repository.insert(account.customer.address)
        account.customer.address = address
        customer = self.customer_repository.insert(account.customer)
        account.customer = customer
        #customer = self.product_respository.get_by_id(account.customer.id)
        #account.customer = customer
        #account.total = account.customer.unit_cost * account.quantity
        return self.order_repository.insert(account)

    def get_all_accounts (self) -> 'list [Account]':
        accounts = self.account_repository.get_all()
        for account in accounts:
            account.customer = self.customer_repository.get_by_id (account.customer.id)
            account.customer.address = self.address_repository.get_by_id (account.customer.address.id)
        return accounts


    def get_account (self, account_number: str) -> Account:
        account = self.account_repository.get_by_account_number (account_number)
        account.customer = self.customer_repository.get_by_id(account.customer.id)
        account.customer. address = self.address_repository.get_by_id (account.customer.address.id)
        return account

    def withdraw(self, account_number: str, amount: float) -> Account:
        account = self.account_repository.get_by_account_number (account_number)
        account.current_balance -= amount
        self.account_repository.update (account)
        return self.get_account (account_number) 
        




